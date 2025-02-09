from abc import ABC, abstractmethod
from time import time, sleep


class State(ABC):
    created_time = time()

    @abstractmethod
    def handle(self, context):
        pass
    
    def refresh_time(self):
        self.created_time = time()


class OnState(State):
    def handle(self, context):
        print("Камера в состоянии On")
        created_time = context.get_state_creation_time()
        current_time = time()

        # если включено больше 2 секунд то изменить состояние на StandBy
        if current_time - created_time > 2:
            context.set_state(StandByState())
            self.refresh_time()


class OffState(State):
    created_time = None

    def handle(self, context):
        print("Камера в состоянии Off")
        context.set_state(OnState())  # Возвращаемся к предыдущему состоянию


class StandByState(State):
    def handle(self, context):
        print("Камера в состоянии Stand By")
        context.set_state(OnState())


class VideoCamera:
    def __init__(self, state: State):
        self._state = state

    def set_state(self, state: State):
        print(f"Состояние изменено на {state.__class__.__name__}")
        self._state = state

    def get_state_creation_time(self):
        return self._state.created_time

    def request(self):
        self._state.handle(self)


if __name__ == "__main__":
    # Начинаем с состояния On
    context = VideoCamera(OnState())
    context.request()  # Камера в состоянии On
    sleep(3)
    context.request()  # Камера в состоянии StandBy
    context.request()
    context.set_state(OffState())  # Камера в состоянии Off
