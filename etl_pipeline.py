import sqlalchemy


# str = "sqlite:///meta_dwh.db"

class MetaETLPipeline:
    def __init__(self, db_url: str, trino_host: str, trino_port: int, trino_user: str, trino_catalog: str):
        self.engine = sqlalchemy.create_engine(db_url, echo=False)
        self.trino_host = trino_host
        self.trino_port = trino_port
        self.trino_user = trino_user
        trino_url = f"trino::/{self.trino_user}@{self.trino_host}:{trino_port}/{trino_catalog}"
        self.trino_engine = sqlalchemy.create_engine(trino_url, echo=False)

    def extraction(self, target_date: str) -> dict:
        hrdb_query = sqlalchemy.text("SELECT id, name , team , role, date_of_birth FROM hrdb")
        date_query = sqlalchemy.text("SELECT id, year, month , day ")

        with open("queries.sql", "r", encoding="utf-8") as f:
            iceberg_query = sqlalchemy.text(f.read())

        with self.engine.connect() as conn:
            hr_db = [dict(row) for row in conn.execute(hrdb_query).mappings().all()]
            dates_db = [dict(row) for row in conn.execute(date_query).mappings().all()]

        with self.trino_engine.connect() as trino_conn:
            trino_result = trino_conn.execute(iceberg_query, {"target_date": target_date}).mappings().all()

        return {
            "hrdb": hr_db,
            "dates": dates_db,
            "iceber": trino_result
        }

    def transformation(self):
        pass

    def load(self):
        pass

    def etl(self):
        pass
