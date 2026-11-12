from metadwh import Dates
from metadwh import HRDB
import sqlalchemy
import sqlalchemy.orm
import faker


# "sqlite:///meta_dwh.db"

class Seeding:
    def __init__(self, db_url: str):
        self.engine = sqlalchemy.create_engine(db_url, echo=False)
        self.fake = faker.Faker()

    def seeding_date(self):
        with sqlalchemy.orm.Session(self.engine) as session:
            for i in range(2026, 2031, 1):
                for j in range(1, 13, 1):
                    match j:
                        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                            days = 31
                        case 4 | 6 | 9 | 11:
                            days = 30
                        case 2:
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

    def seeding_hrdb(self):
        with sqlalchemy.orm.Session(self.engine) as session:
            for _ in range(100):
                new_person = HRDB(
                    id=self.fake.uuid4(),
                    name=self.fake.name(),
                    team=self.fake.word().capitalize(),
                    role=self.fake.job().capitalize(),
                    date_of_birth=self.fake.date_of_birth(minimum_age=18, maximum_age=60),
                    payday=self.fake.random_int(min=2240, max=20000),
                    reputation=self.fake.random_int(min=1, max=100),
                    exp=self.fake.random_element(elements=('Junior', 'Middle', 'Senior'))

                )
                session.add(new_person)

            session.commit()
