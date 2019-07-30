'''Demonstrates lazily reading lines of file using generator'''
from os import path


def read_lines(file_path):
    if is_valid(file_path):
        file = open(file_path.strip(), 'r')
        line = file.readline()
        while line:
            print('read line...!!!')
            yield line
            line = file.readline()


def is_valid(file_path):
    if file_path != None and len(file_path.strip()) > 0 and path.exists(file_path) and path.isfile(file_path):
        return True
    else:
        return False


if __name__ == '__main__':
    for line in read_lines('test_file.txt'):
        print('received the line')
        print(line)
