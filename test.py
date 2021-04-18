import re

def conform(value):
    return re.match(r"^([a-z0-9]{3,20}[^-])$", value)


if __name__ == "__main__":
    correct = 'test654364'
    wrong  = 'test87--'
    print(conform(correct))
    print(conform(wrong))
