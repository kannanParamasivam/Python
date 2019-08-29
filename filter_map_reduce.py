from typing import List
from functools import reduce


def get_even_numbers(nums: List[int]):
    # return list(filter(is_even, nums)) # External method to filter
    return list(filter(lambda n: n%2 == 0, nums))

def is_even(n:int):
    return n%2 == 0


def add_two(nums:List[int]):
    # return list(map(add_number, nums)) # External method to map
    return list(map(lambda n: n+2, nums))


def add_number(n):
    return n+2


def add_all(nums:List[int]):
    # return reduce(add_nums, nums) # External method to reduce
    return reduce(lambda a,b: a+b, nums)


def add_nums(a, b):
    return a+b