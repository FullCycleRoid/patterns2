from abc import ABC, abstractmethod


class Robot:
    def move_forward(self):
        print("Робот движется вперед")

    def move_backward(self):
        print("Робот движется назад")

    def pick_up_object(self):
        print("Робот поднимает предмет")

    def put_down_object(self):
        print("Робот опускает предмет")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class MoveForwardCommand(Command):
    def __init__(self, robot: "Robot"):
        self.robot = robot

    def execute(self):
        self.robot.move_forward()

    def undo(self):
        self.robot.move_backward()


class MoveBackwardCommand(Command):
    def __init__(self, robot: "Robot"):
        self.robot = robot

    def execute(self):
        self.robot.move_backward()

    def undo(self):
        self.robot.move_forward()


class PickUpObjectCommand(Command):
    def __init__(self, robot):
        self.robot = robot

    def execute(self):
        self.robot.pick_up_object()

    def undo(self):
        self.robot.put_down_object()


class PutDownObjectCommand(Command):
    def __init__(self, robot):
        self.robot = robot

    def execute(self):
        self.robot.put_down_object()

    def undo(self):
        self.robot.pick_up_object()

class RemoteControl:
    def __init__(self):
        self.command = None
        self.history = []

    def set_command(self, command: "Command"):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()
            self.history.append(self.command)

    def press_undo(self):
        if self.history:
            last_command = self.history.pop()
            last_command.execute()
а р


# Создание робота
robot = Robot()

# Создание команд
move_forward = MoveForwardCommand(robot)
move_backward = MoveBackwardCommand(robot)
pick_up = PickUpObjectCommand(robot)
put_down = PutDownObjectCommand(robot)

# Создание удалённого пульта
remote = RemoteControl()

# Назначение команды на кнопку
remote.set_command(move_forward)
remote.press_button()  # Вывод: Робот движется вперед

remote.set_command(pick_up)
remote.press_button()  # Вывод: Робот поднимает предмет

# Отмена последней команды
remote.press_undo()  # Вывод: Робот опускает предмет

remote.set_command(move_backward)
remote.press_button()  # Вывод: Робот движется назад

# Отмена всех команд
while remote.history:
    remote.press_undo()  # Последовательно отменяет все выполненные команды