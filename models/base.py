from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from __future__ import annotations

engine = create_engine("sqlite:///my_db.db", echo=True)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    # @classmethod
    # @property
    # def __tablename__(cls):
    #     return f"{cls.__name__}s"


def up():
    Base.metadata.create_all(bind=engine)


def down():
    Base.metadata.drop_all(bind=engine)
