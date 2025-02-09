from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class Lada(Car):
    def drive(self):
        return 'Lada driving forward'

class BMW(Car):
    def drive(self):
        return 'BMW driving forward'

class Audi(Car):
    def drive(self):
        return 'Audi driving forward'

class AbstractFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass

class LadaFactory(AbstractFactory):
    def create_car(self) -> Lada:
        return Lada()

class BMWFactory(AbstractFactory):
    def create_car(self) -> BMW:
        return BMW()

class AudiFactory(AbstractFactory):
    def create_car(self) -> Audi:
        return Audi()

factory = BMWFactory()
BMW = factory.create_car()
print(BMW.drive())
