import sqlalchemy
# "sqlite:///meta_dwh.db"

class MetaETLPipeline:
    def __init__(self, db_url: str):
        self.engine = sqlalchemy.create_engine(db_url, echo=False)

    def extraction(self) -> list[dict]:
        pass

    def transformation(self):
        pass

    def load(self):
        pass

    def etl(self):
        pass
