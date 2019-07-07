from util import print_banner as pb


def get_length(s):
    pb("Length")
    print(len(s))


def concat(s1, s2):
    pb("Concat with Plus")
    s = s1+s2
    print(s)
    pb("Concat with join")
    s = "".join((s1, s2))
    print(s)
    s = " ".join((s1, s2))
    print(s)


def main():
    s = "this is the sample string"
    pb("string")
    print(s)
    get_length(s)
    concat("coffee", "cup")


if __name__ == "__main__":
    main()
