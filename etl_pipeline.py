import sqlalchemy


# str = "sqlite:///meta_dwh.db"

class MetaETLPipeline:
    def __init__(self, db_url: str, trino_host: str, trino_port: int, trino_user: str):
        self.engine = sqlalchemy.create_engine(db_url, echo=False)
        self.trino_host = trino_host
        self.trino_port = trino_port
        self.trino_user = trino_user

    def extraction(self) -> list[dict]:
        with self.engine.connect() as conn:
            pass


    def transformation(self):
        pass

    def load(self):
        pass

    def etl(self):
        pass
