from tkinter import BaseWidget
from datetime import date
import sqlalchemy
from sqlalchemy import create_engine, Integer
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Date
import uuid


class Base(DeclarativeBase):
    pass


class User(Base):
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    team: Mapped[str] = mapped_column(String(20))
    role: Mapped[str] = mapped_column(String(20))
    date_of_birth: Mapped[date] = mapped_column(Date)


class Tables(Base):
    id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.Uuid, primary_key=True, default=uuid.uuid4())
    table_name: Mapped[str] = mapped_column(String(25))


class Dates(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    year: Mapped[int] = mapped_column(Integer)
    month: Mapped[int] = mapped_column(Integer)
    day: Mapped[int] = mapped_column(Integer)


class facts(Base):
    id_person: Mapped[uuid.UUID] = mapped_column(sqlalchemy.Uuid)
    table_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.Uuid)
    date_id: Mapped[int] = mapped_column(Integer)
    maxpeakmemory_bytes: Mapped[int] = mapped_column(Integer)
    processed_input_lines: Mapped[int] = mapped_column(Integer)
    bytes_read: Mapped[int] = mapped_column(Integer)
    queued_time: Mapped[int] = mapped_column(Integer)
    whole_time_query: Mapped[int] = mapped_column(Integer)
    spilled_bytes: Mapped[int] = mapped_column(Integer)


def tablescreation(self):
    engine = create_engine("sqlite://", echo=False)
