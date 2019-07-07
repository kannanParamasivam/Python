"""Expressions for default valued params will be executed only once when def statement is executed"""

from time import sleep, ctime


def show_current_time(arg=ctime()):
    print(arg)


def show_current_time_solution(arg=None):
    if arg != None:
        print(arg)


def main():
    for i in range(6):
        show_current_time()
        sleep(1)

    for i in range(6):
        show_current_time_solution(ctime())
        sleep(1)


if __name__ == "__main__":
    main()
