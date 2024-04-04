from typing import List
from . import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Car(Base):
    __tablename__ = "car"
    brand: Mapped[str]
    model_name: Mapped[str]
    wheels: Mapped[List["Wheel"]] = relationship(back_populates="car")

    def __repr__(self) -> str:
        return (
            f"{self.brand}[{self.model_name}]\nwheels:{[str(x) for x in self.wheels]}"
        )
