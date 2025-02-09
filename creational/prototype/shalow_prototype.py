import copy

# Абстрактный прототип (интерфейс)
class Prototype:
    def clone(self):
        pass

# Конкретный прототип
class ConcretePrototype(Prototype):
    def __init__(self, name):
        self.name = name

    def clone(self):
        # Используем shallow copy (поверхностное копирование)
        return copy.copy(self)

    def __str__(self):
        return f"ConcretePrototype(name={self.name})"

if __name__ == "__main__":
    prototype = ConcretePrototype("Original")
    print(f"Original Object: {prototype}")

    cloned_prototype = prototype.clone()
    cloned_prototype.name = "Cloned"
    print(f"Cloned Object: {cloned_prototype}")