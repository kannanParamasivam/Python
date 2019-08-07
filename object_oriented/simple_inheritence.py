from util import print_banner as pb
from sys import path
from os.path import dirname
path.append(dirname(dirname(__file__)))


class Employee:
    """Parent class"""
    raise_rate = 1.04

    def __init__(self, fn, ln, pay):
        self._fn = fn
        self._ln = ln
        self._pay = pay

    def get_fullname(self):
        return '{0} {1}'.format(self._fn, self._ln)

    def apply_raise(self):
        self._pay = self._pay * self.raise_rate


class Developer(Employee):
    """Child class"""

    raise_rate = 1.10

    def __init__(self, fn, ln, pay, prog_lang):
        super().__init__(fn, ln, pay)
        self._prog_lang = prog_lang

    def get_prog_lang(self):
        return self._prog_lang


class Manager(Employee):
    """Child class"""

    def __init__(self, fn, ln, pay, emps=None):
        super().__init__(fn, ln, pay)
        self._emps = emps

    def print_emps(self):
        for emp in self._emps:
            print('--> {}'.format(emp.get_fullname()))
        print('\n')

    def add_emp(self, emp):
        self._emps.append(emp)

    def remove_emp(self, emp):
        if emp in self._emps:
            self._emps.remove(emp)


emp = Employee('kannan', 'sivam', 50000)
pb(emp.get_fullname())
print(emp._pay)
emp.apply_raise()
print(emp._pay)
print('\n')

dev = Developer('Kannan', 'Dev', 50000, 'csharp')
pb(dev.get_fullname())
print(dev._pay)
dev.apply_raise()
print(dev._pay)
print(dev.get_prog_lang())
print('\n')

mgr = Manager('Kannan', 'Mgr', 50000, [emp])
pb(mgr.get_fullname())
print(mgr._pay)
mgr.apply_raise()
print(mgr._pay)
mgr.print_emps()
mgr.add_emp(dev)
mgr.print_emps()
mgr.remove_emp(emp)
mgr.print_emps()
print('\n')

if isinstance(dev, Developer):
    print("dev is Developer")

if isinstance(dev, Employee):
    print('dev is Employee')

if isinstance(mgr, Manager):
    print('mgr is Manager')

if isinstance(mgr, Developer):
    print('mgr is developer')
else:
    print('mgr is not developer')

if issubclass(Developer, Employee):
    print('Developer is subclass of Employee')

if issubclass(Employee, Developer):
    print('Employee is subclass of Developer')
else:
    print('Employee is not subclass of Developer')
