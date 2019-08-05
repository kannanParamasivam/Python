from pprint import pprint as pp
from os.path import dirname, abspath
from sys import path
path.append(dirname(dirname(abspath(__file__))))
from util import print_banner as pb

class Employee:
    raise_rate = 1.04

    def __init__(self, fn, ln, pay):
        self.fn = fn
        self.ln = ln
        self.pay = pay


class Developer(Employee):
    def __init__(self, fn, ln, pay, prog_lang):
        super().__init__(fn, ln, pay)
        self.prog_lang = prog_lang


pb('employee')
emp = Employee('kannan', 'Paramasivam', 50000)
pp(emp.__dict__)

pb('developer')
dev = Developer('Kan', 'Sivam', 50000, 'python')
pp(dev.__dict__)
import os
print(os.__file__)

