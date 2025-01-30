from typing import Protocol

class Loggable(Protocol):
	def log(self, text: str) -> None: ...

class FileLogger:
	def __init__(self, filename: str) -> None:
		self.filename: str = filename

	def log(self, text: str) -> None:
		with open(self.filename, 'a') as file:
			file.write(f'{text}\n')


class ConsoleLogger:
	def log(self, text: str) -> None:
		print(text)


def logger(logger: Loggable, text: str):
	logger.log(text)


logger(ConsoleLogger(), 'oops')