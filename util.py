def print_banner(message, border_char="*"):
    border = border_char*len(message)
    print('\n{}'.format(border))
    print(message)
    print(border)
