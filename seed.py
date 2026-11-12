import sqlalchemy
import sqlalchemy.orm
# "sqlite:///meta_dwh.db"

class Fulling:
    def __init__(self, db_url: str):
        self.engine = sqlalchemy.create_engine(db_url, echo=False)

    def fulling_date(self):
        with sqlalchemy.orm.Session(self.engine) as session:
            pass
