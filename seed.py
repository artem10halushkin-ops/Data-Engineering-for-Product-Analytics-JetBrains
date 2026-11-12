from metadwh import Dates
import sqlalchemy
import sqlalchemy.orm


# "sqlite:///meta_dwh.db"

class Fulling:
    def __init__(self, db_url: str):
        self.engine = sqlalchemy.create_engine(db_url, echo=False)

    def fulling_date(self):
        with sqlalchemy.orm.Session(self.engine) as session:
            dates_batch = []
            for i in range(2026, 2031, 1):
                for j in range(1, 13, 1):
                    match j:
                        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                            days = 31
                        case 4 | 6 | 9 | 11:
                            days = 30
                        case (2):
                            match i:
                                case year if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                                    days = 29
                                case _:
                                    days = 28
                    for z in range(1, days + 1):
                        new_id = z + 100 * j + i * 10000

                        new_date = Dates(id=new_id, year=i, month=j, day=z)
                        session.add(new_date)

                session.commit()
