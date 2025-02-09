from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"

if __name__ == "__main__":
    leaf1 = Leaf()
    leaf2 = Leaf()

    composite1 = Composite()
    composite1.add(leaf1)
    composite1.add(leaf2)

    leaf3 = Leaf()
    composite2 = Composite()
    composite2.add(leaf3)

    composite1.add(composite2)

    print(composite1.operation())