"""Demonstrates default valued, positional and key word parameters"""


def print_banner(message, border='-'):
    border_line = border*len(message)
    print(border_line)
    print(message)
    print(border_line)


def main():
    print_banner('default valued banner character')
    print_banner('overwritten default value of argument', '*')
    print_banner(border="#", message="key word arguments")
    print_banner("positional argument and keyword argument", border="=")


if __name__ == "__main__":
    main()
