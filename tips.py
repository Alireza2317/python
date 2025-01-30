# list slicing
nums = list(range(10))
print(nums)
print(nums[-2:])
print(nums[5:1:-2])



# lambda
div = lambda x: 2*x
div(8)



# forced positional and keyword params
def function(x, y, /, z, *, k):
	#* x and y should only be passed positionally
	#* z can be passed in both formats
	#* k should only be passed by keywords

	return x + y + z + k

print(function(1, 2, 3, k=5))
print(function(1, 2, z=3, k=5))




# saving the slice
rev = slice(None, None, 2)

nums = list(range(10))

nums[rev]




# sets math
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7}

print(set_a | set_b) #* union
print(set_a - set_b) #* difference
print(set_a ^ set_b) #* symmetric difference
print(set_a & set_b) #* intersection





# f-strring specifier

class Book:
	def __init__(self, title: str, pages: int) -> None:
		self.title = title
		self.pages = pages

	def __format__(self, __format_spec: str) -> str:
		match __format_spec:
			case 'time':
				return f'{self.pages / 60:.2f} hours'
			case 'caps':
				return self.title.upper()


book = Book('Of Mice and Men', 200)

print(f'this book is named: {book:caps} and it would take {book:time} to read!')







# wallrus operator

#! example without wallrus
users = {
	0: 'Bob',
	1: 'Mario'
}
user = users.get(3)
if user:
	print(f'user {user} exists')
else:
	print('doesnt exist')


#* wallrus -> assignment and outputing at the same time
if user := users.get(1):
	print(f'user {user} exists')
else:
	print('doesnt exist')


#* it can be used anywhere, not just in an if statement







# functional programming ideas
from typing import Callable

def multiplier(a: float) -> Callable:
	def multiply(b: float):
		return a * b

	return multiply

doubler = multiplier(2)
tripler = multiplier(3)

print(doubler(23))
print(tripler(17))