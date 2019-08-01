class Employee:
    def __init__(self, name, age, phone, city):
        self.name = name
        self.age = age
        self.phone = phone
        self.city = city


emp1 = Employee('Kannan', 32, '224-280-2046', 'Chicago')
print('name: {name} \n age: {age}'.format(name=emp1.name, age=emp1.age))
