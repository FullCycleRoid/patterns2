import copy

class ComplexObject:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"ComplexObject(data={self.data})"

class Prototype:
    def clone(self):
        pass

class ConcretePrototype(Prototype):
    def __init__(self, name, complex_object):
        self.name = name
        self.complex_object = complex_object

    def clone(self):
        # Используем deep copy для вложенных объектов
        return copy.deepcopy(self)

    def __str__(self):
        return f"ConcretePrototype(name={self.name}, complex_object={self.complex_object})"

# Клиентский код
if __name__ == "__main__":
    complex_data = ComplexObject([1, 2, 3])
    prototype = ConcretePrototype("Original", complex_data)
    print(f"Original Object: {prototype}")

    cloned_prototype = prototype.clone()
    cloned_prototype.name = "Cloned"
    cloned_prototype.complex_object.data[0] = 999
    print(f"Cloned Object: {cloned_prototype}")
    print(f"Original Object after cloning: {prototype}")