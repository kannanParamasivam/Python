from os.path import dirname
from sys import path
path.append(dirname(dirname(__file__)))
from util import print_banner as pb

class Employee:
	
	def __init__(self, fn, ln):
		self._fn = fn
		self._ln = ln

	@property	
	def fullname(self):
		return '{} {}'.format(self._fn, self._ln)

	@fullname.setter
	def fullname(self, name):
		fn, ln = name.split()
		self._fn = fn
		self._ln = ln

	@fullname.deleter
	def fullname(self):
		self._fn = None
		self._ln = None

	@property
	def email(self):
		return '{}.{}@email.com'.format(self._fn, self._ln)

emp = Employee('Kannan', 'Sivam')
print(emp.fullname)
print(emp.email)

emp._fn = 'John'
emp._ln = 'Bowman'
print(emp.fullname)
print(emp.email)

emp.fullname = 'kannan sivam'
print(emp.fullname)
print(emp.email)

del emp.fullname
print(emp.fullname)
print(emp.email)