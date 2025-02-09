from abc import ABC, abstractmethod


class AbstractPetFood(ABC):
    @abstractmethod
    def feed(self):
        pass

class DogFood(AbstractPetFood):
    def feed(self):
        return 'Dog food'

class CatFood(AbstractPetFood):
    def feed(self):
        return 'Cat food'


class AbstractPet(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(AbstractPet):
    def speak(self):
        return 'Dog say woof'

class Cat(AbstractPet):
    def speak(self):
        return 'Cat say meau'


class AbstractFactory(ABC):
    @abstractmethod
    def create_pet(self) -> AbstractPet:
        pass

    @abstractmethod
    def create_pet_food(self) -> AbstractPetFood:
        pass

class DogFactory(AbstractFactory):
    def create_pet(self) -> Dog:
        return Dog()

    def create_pet_food(self) -> DogFood:
        return DogFood()


class CatFactory(AbstractFactory):
    def create_pet(self) -> CatFood:
        return Cat()

    def create_pet_food(self) -> Cat:
        return CatFood()


factory = DogFactory()
pet = factory.create_pet()
food = factory.create_pet_food()

print(pet.speak())
print(food.feed())