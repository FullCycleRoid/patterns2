import copy

class PrototypeRegistry:
    def __init__(self):
        self._prototypes = {}

    def register(self, name, prototype):
        self._prototypes[name] = prototype

    def unregister(self, name):
        del self._prototypes[name]

    def create(self, name, **kwargs):
        prototype = self._prototypes.get(name)
        if not prototype:
            raise ValueError(f"Prototype '{name}' not found.")
        # Используем метод clone объекта-прототипа
        new_obj = prototype.clone()
        new_obj.__dict__.update(kwargs)  # Обновляем атрибуты при необходимости
        return new_obj

class Prototype:
    def clone(self):
        # По умолчанию используем deepcopy
        return copy.deepcopy(self)

class ConcretePrototypeA(Prototype):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def clone(self):
        # Реализуем собственный метод клонирования
        new_instance = ConcretePrototypeA(self.name, self.value)
        # Можно добавить дополнительную логику здесь
        return new_instance

    def __str__(self):
        return f"ConcretePrototypeA(name={self.name}, value={self.value})"

class ConcretePrototypeB(Prototype):
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def clone(self):
        # Реализуем собственный метод клонирования
        new_instance = ConcretePrototypeB(self.name, copy.deepcopy(self.data))
        # Можно добавить дополнительную логику здесь
        return new_instance

    def __str__(self):
        return f"ConcretePrototypeB(name={self.name}, data={self.data})"

# Клиентский код
if __name__ == "__main__":
    registry = PrototypeRegistry()

    # Регистрируем прототипы
    prototype_a = ConcretePrototypeA("DefaultA", 42)
    prototype_b = ConcretePrototypeB("DefaultB", [1, 2, 3])

    registry.register("A", prototype_a)
    registry.register("B", prototype_b)

    # Создаем новые объекты на основе прототипов
    obj_a = registry.create("A", name="CustomA", value=100)
    obj_b = registry.create("B", name="CustomB", data=[4, 5, 6])

    print(obj_a)
    print(obj_b)