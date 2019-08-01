from pprint import pprint


class Employee:
    # Class variables
    raise_amount = 1.05
    number_of_employees = 0

    def __init__(self, firstName, lastName, age, phone, city, pay):
        # Instance variables
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.phone = phone
        self.city = city
        self.pay = pay
        Employee.number_of_employees += 1

    def getfullname(self):
        return "{fn} {ln}".format(fn=self.firstName, ln=self.lastName)

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

emp1 = Employee('Kannan', 'Paramasivam', 32, '224-280-2046', 'Chicago', 50000)
print('Number of employees (emp1) : {}'.format(emp1.number_of_employees))

print('First Name: {fn} \nLast Name: {ln}'.format(
    fn=emp1.firstName, ln=emp1.lastName))

# Two ways of calling instance specific methods
print('Full Name: {}'.format(emp1.getfullname()))
print('Full Name: {}'.format(Employee.getfullname(emp1)))

emp2 = Employee('James', 'Baker', 46, '254-345-7346', 'Tampa', 60000)
print('Number of employees (emp2) : {}'.format(emp2.number_of_employees))

# Show instance members
pprint(emp1.__dict__)
pprint(emp2.__dict__)

# Show Class members
pprint(Employee.__dict__)

# Access class member through instance
print('emp1 raise: {0}\nemp2 raise: {1}'.format(
    emp1.raise_amount, emp2.raise_amount))

# Use class member in instance method
emp1.apply_raise()
pprint(emp1.__dict__)
pprint(emp2.__dict__)

# override class memeber by instance member
emp1.raise_amount = 1.10
emp1.apply_raise()
# Notice raise_amout is included in the isnstance memeber but not to emp2
pprint(emp1.__dict__)
pprint(emp2.__dict__)

# Class member is used to track number of instances (singleton)
print('Number of employees: {}'.format(Employee.number_of_employees))
print('Number of employees (emp1) : {}'.format(emp1.number_of_employees))
print('Number of employees (emp2) : {}'.format(emp2.number_of_employees))