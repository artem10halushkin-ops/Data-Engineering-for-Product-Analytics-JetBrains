from tkinter import BaseWidget

import sqlalchemy
from sqlalchemy import create_engine
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass

class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    team: Mapped[str] = mapped_column(String(20))
    role: Mapped[str] = mapped_column(String(20))



def tablescreation(self):

    engine = create_engine("sqlite://" , echo=False)

