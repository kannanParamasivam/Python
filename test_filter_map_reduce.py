import unittest
from typing import List
from filter_map_reduce import *

class TestFilterMapReduce(unittest.TestCase):


    def setUp(self):
        pass

    
    def tearDown(self):
        pass

    
    def test_get_even_numbers(self):
        self.assertEqual(get_even_numbers([1,2,3,4,5,6,7,8,9]), [2,4,6,8]) 

    
    def test_add_two(self):
        self.assertEqual(add_two([1,2,3]),[3,4,5])

    def test_add_all(self):
        res = add_all([1,2,3])
        self.assertEqual(res, 6)


if __name__ == '__main__':
    unittest.main()

