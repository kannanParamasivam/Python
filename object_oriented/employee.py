class Employee:
    def __init__(self, firstName, lastName, age, phone, city):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.phone = phone
        self.city = city

    def getfullname(self):
        return "{fn} {ln}".format(fn=self.firstName, ln=self.lastName)


emp1 = Employee('Kannan', 'Paramasivam', 32, '224-280-2046', 'Chicago')

print('First Name: {fn} \nLast Name: {ln}'.format(
    fn=emp1.firstName, ln=emp1.lastName))

# Two ways of calling instance specific methods
print('Full Name: {}'.format(emp1.getfullname()))
print('Full Name: {}'.format(Employee.getfullname(emp1)))
