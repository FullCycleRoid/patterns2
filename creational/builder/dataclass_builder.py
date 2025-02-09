from dataclasses import dataclass

@dataclass
class Car:
    color: str = None
    engine: str = None
    wheels: int = None
    sunroof: bool = False

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_color(self, color):
        self.car.color = color
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_wheels(self, wheels):
        self.car.wheels = wheels
        return self

    def add_sunroof(self):
        self.car.sunroof = True
        return self

    def build(self):
        return self.car

# Использование
builder = CarBuilder()
car = (
    builder
    .set_color("Green")
    .set_engine("Diesel")
    .set_wheels(4)
    .add_sunroof()
    .build()
)
print(car)  # Output: Car(color='Green', engine='Diesel', wheels=4, sunroof=True)