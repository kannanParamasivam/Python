
message = "message from global variable"


def print_message_by_global_variable_name():
    message = "message from local variable with global variable name"
    print(message)


def modify_and_print_message_from_global_variable():
    global message
    message = "modified message at global"


def print_message_from_global_variable_without_explicit_spcifier():
    print(message)


def main():
    print("Calling method which has variable with global variable name")
    print_message_by_global_variable_name()
    print("calling method which explicitly access global variable")
    modify_and_print_message_from_global_variable()
    global message
    print(message)
    message = "message from global variable"
    print("Global variable would be accessed in local scope untill it have been atttempted to be modified")
    print_message_from_global_variable_without_explicit_spcifier()


if __name__ == "__main__":
    main()
