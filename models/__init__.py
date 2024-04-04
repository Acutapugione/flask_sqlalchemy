from .base import Base, up, down, Session
from .car import Car
from .wheel import Wheel


def init():
    with Session.begin() as session:
        cars = {
            Car(brand="BMW", model_name="X6"),
            Car(brand="Mercedes Benz", model_name="W124"),
            Car(brand="Tesla", model_name="Mark-II"),
            Car(brand="Tesla", model_name="Model-Y"),
        }
        for car in cars:
            car.wheels = [Wheel(brand="Michlen", model_name="27''") for i in range(4)]
        session.add_all(cars)


down()
up()
init()
