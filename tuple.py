from util import print_banner


def demo_tuple():
    t = ("some string value", 2.3, 3)
    print_banner("This is tuple")
    print(t)
    print_all_elements(t)
    print_nth_element(t, 1)
    t_nested = ((1, 2), (3, 4), (5, 6))
    print_banner("Nested tuple")
    print(t_nested)
    print_nmth_element(t_nested, 2, 1)
    print_banner("Return more than one value as tuple")
    t = find_minmax((4, 6, 2, 3))
    print(t, "is of type", type(t))
    print_banner("Unpack values of tuple")
    min, max = t
    print("min is ", min, " max is ", max)


def print_all_elements(t):
    print_banner("Printing all elements in tuple")
    for item in t:
        print(item)


def print_nth_element(t, n):
    print_banner(str(n) + "th element")
    if n < len(t):
        print(t[n])
    else:
        print("Index out of bounds")


def print_nmth_element(t, n, m):
    print_banner("Print "+str(m)+"th child of "+str(n)+"th child tuple")
    if t != None and len(t) > 0 and n < len(t) and m < len(t[n]):
        print(t[n][m])
    else:
        print("Could not locate the element")


def find_minmax(t):
    print("Calculating min and max of ", t)
    return min(t), max(t)


def main():
    demo_tuple()


if __name__ == "__main__":
    main()
