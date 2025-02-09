class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, extrinsic_state):
        print(f"Shared State: {self.shared_state}, Extrinsic State: {extrinsic_state}")


class FlyweightFactory:
    _flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self._flyweights:
            self._flyweights[shared_state] = Flyweight(shared_state)
        return self._flyweights[shared_state]

    def list_flyweights(self):
        return self._flyweights.keys()

def add_to_database(factory, shared_state, extrinsic_state):
    flyweight = factory.get_flyweight(shared_state)
    flyweight.operation(extrinsic_state)


factory = FlyweightFactory()

add_to_database(factory, "Button", "Window1")
add_to_database(factory, "Button", "Window2")
add_to_database(factory, "Label", "Window1")

print("Unique Flyweights:", factory.list_flyweights())