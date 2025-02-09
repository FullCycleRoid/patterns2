class Originator:
    def __init__(self):
        self._state = ""

    def set_state(self, state):
        """Устанавливаем новое состояние"""
        print(f"Originator: Состояние изменено на '{state}'")
        self._state = state

    def save_to_memento(self):
        """Сохраняем текущее состояние в Memento"""
        print("Originator: Сохранение состояния...")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        """Восстанавливаем состояние из Memento"""
        self._state = memento.get_saved_state()
        print(f"Originator: Состояние восстановлено до '{self._state}'")


class Memento:
    def __init__(self, state):
        """Сохраняем состояние"""
        self._state = state

    def get_saved_state(self):
        """Получаем сохранённое состояние"""
        return self._state


class Caretaker:
    def __init__(self):
        """Инициализируем список для хранения состояний"""
        self._mementos = []

    def add_memento(self, memento):
        """Добавляем новое состояние"""
        self._mementos.append(memento)
        print("Caretaker: Состояние сохранено.")

    def get_memento(self, index):
        """Получаем сохранённое состояние по индексу"""
        return self._mementos[index]


# Пример использования
if __name__ == "__main__":
    originator = Originator()  # Создаём объект Originator
    caretaker = Caretaker()    # Создаём объект Caretaker для управления состояниями

    originator.set_state("Первый вариант")  # Устанавливаем начальное состояние
    caretaker.add_memento(originator.save_to_memento())  # Сохраняем состояние

    originator.set_state("Второй вариант")  # Изменяем состояние
    caretaker.add_memento(originator.save_to_memento())  # Сохраняем новое состояние

    originator.set_state("Третий вариант")  # Изменяем состояние ещё раз

    print("\nОтмена последнего изменения:")
    originator.restore_from_memento(caretaker.get_memento(-1))  # Возвращаемся к предыдущему состоянию

    print("\nОтмена ещё одного изменения:")
    originator.restore_from_memento(caretaker.get_memento(-2))  # Возвращаемся ещё дальше