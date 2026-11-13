import sqlalchemy
import uuid


# str = "sqlite:///meta_dwh.db"

class MetaETLPipeline:
    def __init__(self, db_url: str, trino_host: str, trino_port: int, trino_user: str, trino_catalog: str):
        self.engine = sqlalchemy.create_engine(db_url, echo=False)
        self.trino_host = trino_host
        self.trino_port = trino_port
        self.trino_user = trino_user
        trino_url = f"trino://{self.trino_user}@{self.trino_host}:{trino_port}/{trino_catalog}"
        self.trino_engine = sqlalchemy.create_engine(trino_url, echo=False)

    def extraction(self, target_date: str) -> dict:
        hrdb_query = sqlalchemy.text("SELECT id, name , team , role, date_of_birth FROM hrdb")
        date_query = sqlalchemy.text("SELECT id, year, month , day  FROM dates")

        with open("extract_trino.sql", "r", encoding="utf-8") as f:
            iceberg_query = sqlalchemy.text(f.read())

        with self.engine.connect() as conn:
            hr_db = [dict(row) for row in conn.execute(hrdb_query).mappings().all()]
            dates_db = [dict(row) for row in conn.execute(date_query).mappings().all()]

        with self.trino_engine.connect() as trino_conn:
            trino_result = trino_conn.execute(iceberg_query, {"target_date": target_date}).mappings().all()

        return {
            "hrdb": hr_db,
            "dates": dates_db,
            "iceberg": trino_result
        }

    def transformation(self, target_date: str, dbs: dict):
        facts_for_load = []
        tables_for_load = []
        tables_cache = {}
        date_to_int = int(target_date.replace(",", ""))

        hrdb_raw = dbs.get("hrdb", [])
        iceberg = dbs.get("iceberg", [])

        user_for_load = []
        for user in hrdb_raw:
            user_for_load.append({
                "id": user["id"],
                "name": user["name"],
                "team": user["team"],
                "role": user["role"],
                "date_of_birth": user["date_of_birth"],
            })

        for log in iceberg:
            t_name = log["table_name"]
            if t_name not in tables_cache:
                new_uuid = uuid.uuid4()

                tables_cache[t_name] = new_uuid
                tables_for_load.append(
                    {
                        "id": new_uuid,
                        "table_name": t_name
                    }
                )

        for log in iceberg:
            facts_for_load.append({
                "person_id": log["person_id"],
                "table_id": tables_cache[log["table_name"]],
                "date_id": date_to_int,
                "maxpeakmemory_bytes": log["maxpeakmemory_bytes"],
                "processed_input_lines": log["processed_input_lines"],
                "bytes_read": log["bytes_read"],
                "queued_time": log["queued_time"],
                "whole_time_query": log["whole_time_query"],
                "spilled_bytes": log["spilled_bytes"],
            })
        return {
            "users": user_for_load,
            "tables": tables_for_load,
            "daily_usage": facts_for_load
        }

    def load(self):
        pass

    def etl(self):
        pass
