import sqlalchemy


# str = "sqlite:///meta_dwh.db"

class MetaETLPipeline:
    def __init__(self, db_url: str, trino_host: str, trino_port: int, trino_user: str):
        self.engine = sqlalchemy.create_engine(db_url, echo=False)
        self.trino_host = trino_host
        self.trino_port = trino_port
        self.trino_user = trino_user

    def extraction(self) -> list[dict]:
        hrdb_query = sqlalchemy.text("SELECT id, name , team , role, date_of_birth FROM hrdb")
        date_query = sqlalchemy.text("SELECT id, year, month , day ")

        with open("queries.sql") as f:
            iceberg_query = sqlalchemy.text(f.read())

        with self.engine.connect() as conn:
            hr_db = conn.execute(hrdb_query)
            dates_db = conn.execute(date_query)





    def transformation(self):
        pass

    def load(self):
        pass

    def etl(self):
        pass
