class Car:
    def __init__(self):
        self.color = None
        self.engine = None
        self.wheel = None

    def __str__(self):
        return f"Car [Color: {self.color}, Engine: {self.engine}, Wheel: {self.wheel}]"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_color(self, color):
        self.car.color = color
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_wheel(self, wheel):
        self.car.wheel = wheel
        return self
    
    def build(self):
        return self.car

car = CarBuilder().set_wheel(4).set_engine('LADA').set_color('Blue').build()
print(car)