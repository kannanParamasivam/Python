from os.path import dirname
from sys import path
path.append(dirname(dirname(__file__)))
from util import print_banner as pb

pb('Dunder add on int')
print(1+2)
print(int.__add__(1, 2))

pb('Dunder add on string')
print('kannan'+' sivam')
print('kannan'.__add__(' sivam'))

class Employee:
	
	def __init__(self, fn, ln, pay):
		self._fn = fn
		self._ln = ln
		self._pay = pay

	def __repr__(self):
		return "Employee('{0}', '{1}', '{2}')".format(self._fn, self._ln, self._pay)

	def __str__(self):
		return "{0} - {1}".format(self._fn, self._ln)

	def __add__(self, other):
		return self._pay + other._pay

emp1 = Employee('kannan', 'sivam', 50000)
emp2 = Employee('Kan', 'siv', 60000)

pb('Dunder repr ,str and add on employee object')
print(emp1)
print(emp1.__repr__())
print(repr(emp1))

print(emp1.__str__())
print(str(emp1))

print(emp1 + emp2)