'''Module Demonstrates exception handling'''
import sys, os

def convert(s):
    '''Try converting string to integer'''
    print(type(s))
    try:
        i = int(s)
        print('Converted String to Integer {0}'.format(i))
    except (ValueError, TypeError) as e:
        print('Exception occured and going to be reraised')
        raise


def divide(divident,divisor):
    
    if divisor == 0:
        raise ValueError('Divisor Can not be zero')

    quotient = divident / divisor
    print('Answer = {}'.format(quotient))


def create_directory(path, dir_name):
    original_path = os.getcwd()
    print('Current directory: {}'.format(os.getcwd()))
    try:
        os.chdir(path)
        print('Current directory: {}'.format(os.getcwd()))
        os.mkdir(dir_name)
    except OSError as e:
        raise
    finally:
        os.chdir(original_path)
        print('Current directory: {}'.format(os.getcwd()))


if __name__=='__main__':
    create_directory('D:\\Kannan\\temp','newdir?')