import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setup class\n')

    @classmethod
    def tearDownClass(cls):
        print('\ntearDown class\n')

    def setUp(self):
        print('setup\n')
        print('Running {}'.format(unittest.TestCase.id(self)))
        self.emp1 = Employee('kannan', 'sivam', 33,
                             '224-253-2523', 'Chicago', 50000)
        self.emp2 = Employee('john', 'baker', 54,
                             '246-563-7332', 'Tampa', 60000)

    def tearDown(self):
        print('\ntearDown\n')
        if hasattr(self, 'emp1'):
            del self.emp1
        if hasattr(self, 'emp2'):    
            del self.emp2
        if hasattr(self, 'emp3'):
            del self.emp3

    def test_getfullname(self):
        self.assertEqual(self.emp1.getfullname(), 'kannan sivam')
        self.assertEqual(Employee.getfullname(self.emp1), 'kannan sivam')

    def test_classvariable_numberofemployees(self):
        self.assertEqual(Employee.number_of_employees, 2)
        self.emp3 = Employee('sam', 'bowman', 65,
                             '324-532-3621', 'NewYork', 70000)
        self.assertEqual(Employee.number_of_employees, 3)

    def test_access_class_members(self):
        self.assertEqual(self.emp1.raise_amount, 1.05)
        self.assertEqual(Employee.raise_amount, 1.05)
        self.emp1.raise_amount = 1.06
        self.assertEqual(self.emp1.raise_amount, 1.06)
        self.assertEqual(Employee.raise_amount, 1.05)


# emp1 = Employee('kannan', 'sivam', 33, '224-280-2046', 'Chicago', 50000)
# print(emp1.__dict__)

if __name__ == '__main__':
    unittest.main()
