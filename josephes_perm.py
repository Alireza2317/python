from collections import deque

NUMBER_OF_PEOPLE: int = 1_000_000
K: int = 3

people: deque[int] = deque(range(1, NUMBER_OF_PEOPLE+1))
order_of_people: list[int] = []

index: int = 0
while people:
	people.rotate(1 - K)
	person = people.popleft()
	order_of_people.append(person)
print(order_of_people)



