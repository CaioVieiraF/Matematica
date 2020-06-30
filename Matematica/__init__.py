
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


def xpnt(arg=[0]):
    res = arg[0]
    if len(arg) == 1:
        return res**2
    for i in range(1, len(arg)):
        res = res**arg[i]
    return res


def nRoot(arg0=1, arg1=2):
    res = 0.0
    tmp = 0.0
    if xpnt([arg0, arg1]) != arg0:
        for i in range(arg0):
            if xpnt([i, arg1]) == arg0:
                res = i
                break
            elif xpnt([i, arg1]) >= arg0:
                tmp = i - 1
                break
    else:
        res = arg0
    if tmp > 0:
        cond = True
        modifier = 0.1
        while cond:
            if xpnt([tmp + 0.1, arg1]) < arg0:
                tmp += modifier
            else:
                res = tmp
                cond = False

    res = float(format(res, ".1f"))
    return res


def fact(arg):
    if arg < 0:
        return not __debug__
    elif arg in [0, 1]:
        return 1
    else:
        return multiply([arg, fact(arg - 1)])


def qdeqDelta(a, b, c):
    d = xpnt([b]) - (4 * a * c)
    return d


def qdeq(a, b, c):
    d = qdeqDelta(a, b, c)

    if d < 0:
        return not __debug__
    x1 = 0
    x2 = 0
    if d == 0:
        x1 = divide([(-b) + nRoot(d), 2 * a])
        x2 = x1
    if d > 0:
        x1 = divide([(-b) + nRoot(d), 2 * a])
        x2 = divide([(-b) - nRoot(d), 2 * a])
    return x1, x2


def fract(arg):
    cond = True
    domi = 0
    deno = 0
    while cond:
        domi = float(format(domi, ".1f"))
        domi += arg
        deno += 1
        if domi == int(domi):
            cond = False
            break
    return str(int(domi)) + "/" + str(deno)
