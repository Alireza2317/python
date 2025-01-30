from abc import ABC, abstractmethod


class Animal(ABC):
	@abstractmethod
	def make_sound(self) -> str: ...

	@abstractmethod
	def move(self) -> str: ...


class Dog(Animal):
	def make_sound(self) -> str:
		"""Return the sound made by a dog."""
		return 'Woof'


	def move(self) -> str:
		return 'Walks'


# it is not possible to create an instance of an abstract class
# dog = Animal() -> TypeError
# and it is not possible to create a class that inherits from an abstract class
# and does not implement all abstract methods
# so a Dog class without the move method is not possible -> TypeError


dog = Dog()
print(dog.make_sound())
print(dog.move())