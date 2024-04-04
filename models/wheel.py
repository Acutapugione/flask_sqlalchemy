from . import Base, Car
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Wheel(Base):
    __tablename__ = "wheel"
    brand: Mapped[str]
    model_name: Mapped[str]
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"))
    car: Mapped[Car] = relationship(back_populates="wheels")

    def __repr__(self) -> str:
        return f"{self.brand}[{self.model_name}]"
