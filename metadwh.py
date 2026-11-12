from datetime import date
import sqlalchemy
from sqlalchemy import create_engine, Integer
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Date
import uuid


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    team: Mapped[str] = mapped_column(String(20))
    role: Mapped[str] = mapped_column(String(20))
    date_of_birth: Mapped[date] = mapped_column(Date)


class Tables(Base):
    __tablename__ = "tables"
    id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.Uuid, primary_key=True, default=uuid.uuid4)
    table_name: Mapped[str] = mapped_column(String(25))


class Dates(Base):
    __tablename__ = 'dates'
    id: Mapped[int] = mapped_column(primary_key=True)
    year: Mapped[int] = mapped_column(Integer)
    month: Mapped[int] = mapped_column(Integer)
    day: Mapped[int] = mapped_column(Integer)


class Facts(Base):
    __tablename__ = 'daily_usage'
    id_person: Mapped[uuid.UUID] = mapped_column(sqlalchemy.Uuid, ForeignKey("users.id"), primary_key=True, )
    table_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.Uuid, ForeignKey("tables.id"), primary_key=True)
    date_id: Mapped[int] = mapped_column(Integer, ForeignKey("dates.id"), primary_key=True)
    maxpeakmemory_bytes: Mapped[int] = mapped_column(Integer)
    processed_input_lines: Mapped[int] = mapped_column(Integer)
    bytes_read: Mapped[int] = mapped_column(Integer)
    queued_time: Mapped[int] = mapped_column(Integer)
    whole_time_query: Mapped[int] = mapped_column(Integer)
    spilled_bytes: Mapped[int] = mapped_column(Integer)


# Assumption that we have another db with the personal data from hr department


class HRDB(Base):
    __tablename__ = "hrdb"
    id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(20))
    team: Mapped[str] = mapped_column(String(20))
    role: Mapped[str] = mapped_column(String(20))
    date_of_birth: Mapped[date] = mapped_column(Date)
    payday: Mapped[int] = mapped_column(Integer)
    exp: Mapped[int] = mapped_column(Integer)
    reputation: Mapped[int] = mapped_column(Integer)


def tablescreation():
    engine = create_engine("sqlite:///meta_dwh.db", echo=False)
    Base.metadata.create_all(engine)
