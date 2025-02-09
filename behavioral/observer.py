from abc import ABC, abstractmethod


class TemperatureObserver(ABC):
    @abstractmethod
    def update(self, temperature: float) -> None:
        pass


class AirConditioner(TemperatureObserver):
    def update(self, temperature: float):
        if temperature > 25:
            print(f"Кондиционер: Включаю охлаждение при температуре {temperature}°C")
        else:
            print(f"Кондиционер: Выключаю охлаждение при температуре {temperature}°C")


class Thermostat(TemperatureObserver):
    def update(self, temperature: float) -> None:
        if temperature < 20:
            print(f"Термостат: Включаю отопление при температуре {temperature}°C")
        else:
            print(f"Термостат: Выключаю отопление при температуре {temperature}°C")


class UserInterface(TemperatureObserver):
    def update(self, temperature: float) -> None:
        print(f"Пользовательский интерфейс: Обновляю отображение температуры до {temperature}°C")


class TemperatureSensor(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer: TemperatureObserver) -> None:
        self._observers.append(observer)

    def detach(self, observer: TemperatureObserver) -> None:
        self._observers.remove(observer)

    def notify(self, temperature: float) -> None:
        for observer in self._observers:
            observer.update(temperature)


# Конкретный субъект
class SmartTemperatureSensor(TemperatureSensor):
    def __init__(self):
        super().__init__()
        self._current_temperature = None

    def set_temperature(self, temperature: float) -> None:
        self._current_temperature = temperature
        print(f"Датчик температуры: Температура изменилась до {temperature}°C")
        self.notify(temperature)


sensor = SmartTemperatureSensor()

air_conditioner = AirConditioner()
thermostat = Thermostat()
user_interface = UserInterface()

sensor.attach(air_conditioner)
sensor.attach(thermostat)
sensor.attach(user_interface)

# Изменение температуры
sensor.set_temperature(26)  # Кондиционер включается, термостат выключается
print("-" * 40)
sensor.set_temperature(19)