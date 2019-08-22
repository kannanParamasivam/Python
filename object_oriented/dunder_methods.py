class Employee:

    def __init__(self, fn, ln, pay):
        self._fn = fn
        self._ln = ln
        self._pay = pay

    def get_fullname(self):
        return '{0} {1}'.format(self._fn, self._ln)

    def __str__(self):
        print('string representation of object')
        return '{0} - {1}'.format(self._fn, self._ln)

    def __repr__(self):
        print('representation of object')
        return 'repr {0} {1}'.format(self._fn, self._ln)

    def __add__(self, other):
        return self._pay + other._pay

emp = Employee('Kannan', 'Sivam', 50000)
print(emp.get_fullname())
print(emp)
print(str(emp))
print(repr(emp))

emp1 = Employee('Kan', 'Para', 30000)
print(emp+emp1)
