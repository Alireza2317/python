class Student:
	def __init__(self, name: str, grades: list[float]) -> None:
		self.name = name
		self.grades = grades

	def average(self):
		return sum(self.grades) / len(self.grades)

	#def __len__(self):
	#	return len(self.grades)

	def __getitem__(self, index: int):
		return self.grades[index]

	def __repr__(self) -> str:
		return f'<Student: {self.name}>'


st = Student('James', [20, 20, 18, 19, 20])

print(st)


class WorkingStudent(Student):
	def __init__(self, salary, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.salary = salary

	@property
	def annual_salary(self):
		return 12 * 30 * 3 * self.salary

def main():
	wst = WorkingStudent(12, 'Mairo', [20, 10])
	wst.annual_salary


	for item in Student('x', list(range(10, 19))):
		print(item)


	print(type(Student))
	print(type(st))

if __name__ == '__main__':
	main()