def gen():
	yield 1
	yield 2
	yield 3

g = gen()
f = gen()
print(next(g))
print(next(g))
print(next(f))



class Gen:
	def __init__(self) -> None:
		self.number = 0

	def __next__(self):
		if self.number < 3:
			current = self.number
			self.number += 1
			return current
		else:
			raise StopIteration

g = Gen()
print(type(Gen))
print(type(g))

print(next(g))
print(next(g))
print(next(g))
print(next(g))



class GenIter:
	def __init__(self) -> None:
		self.number = 0

	def __next__(self):
		if self.number < 3:
			current = self.number
			self.number += 1
			return current
		else:
			raise StopIteration

	def __iter__(self):
		return self

print(GenIter.__name__)