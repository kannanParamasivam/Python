from pprint import pprint
import datetime
import requests


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
    
    def __del__(self):
        Employee.number_of_employees -= 1

    # Instance method
    def getfullname(self):
        return "{fn} {ln}".format(fn=self.firstName, ln=self.lastName)

    # Instance method
    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

    # Class method which acts as custom constructor
    @classmethod
    def create_employee(cls, emp_details):
        if emp_details != None and len(emp_details.strip()) > 0:
            ls_emp_details = emp_details.split('_')
            if ls_emp_details != None and len(ls_emp_details) == 6:
                fn, ln, age, phone, city, pay = ls_emp_details
                return cls(fn, ln, age, phone, city, pay)
        return None

    # Static method which does not take instance or class as default argument
    @staticmethod
    def is_working_day(date):
        return date.weekday() <= 4

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.lastName}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response'

# # Show instance members
# pprint(emp1.__dict__)
# pprint(emp2.__dict__)

# # Show Class members
# pprint(Employee.__dict__)

# # Access class member through instance
# print('emp1 raise: {0}\nemp2 raise: {1}'.format(
#     emp1.raise_amount, emp2.raise_amount))

# # Use class member in instance method
# emp1.apply_raise()
# pprint(emp1.__dict__)
# pprint(emp2.__dict__)

# # override class memeber by instance member
# emp1.raise_amount = 1.10
# emp1.apply_raise()
# # Notice raise_amout is included in the isnstance memeber but not to emp2
# pprint(emp1.__dict__)
# pprint(emp2.__dict__)

# # Class member is used to track number of instances (singleton)
# print('Number of employees: {}'.format(Employee.number_of_employees))
# print('Number of employees (emp1) : {}'.format(emp1.number_of_employees))
# print('Number of employees (emp2) : {}'.format(emp2.number_of_employees))

# # Creating object using custom cnstructor by class method
# emp3 = Employee.create_employee(
#     'kannan_paramasivam_33_224-280-2046_LakeBluff_50000')
# pprint(emp3.__dict__)

# # Invoking static method
# print('Today is {}'.format('week day' if Employee.is_working_day(datetime.date.today()) else 'week end'))
# print(help(Employee))