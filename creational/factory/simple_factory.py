from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def walk(self): ...


class Man:
    def walk(self):
        return 'Man is walking'

class Women:
    def walk(self):
        return 'Women is walking'


def get_person(person_type: Person):
    _types = {
        "MAN": Man,
        "WOMEN": Women,
    }
    return _types[person_type]() if person_type in _types else 'No persone'


man = get_person('MAN')
animal = get_person('ANIMAL')

print(man.walk())
print(animal)