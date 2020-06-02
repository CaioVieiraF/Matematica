
def add(arg=[0]):
    res = 0
    for i in arg:
        res += i
    return res


def subtract(arg=[0]):
    res = arg[0]
    if len(arg) == 1:
        return 0
    for i in range(1, len(arg)):
        res -= arg[i]
    return res


def multiply(arg=[0]):
    res = 1
    for i in arg:
        res *= i
    return res


def divide(arg=[0]):
    res = arg[0]
    if len(arg) == 1:
        return 0
    for i in range(1, len(arg)):
        res /= arg[i]
    return res
