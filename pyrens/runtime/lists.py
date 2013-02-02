def list_(*args):
    return tuple(args)


def count_(arg1):
    return len(arg1)


def first_(arg1):
    try:
        return arg1[0]
    except IndexError:
        return None


def last_(arg1):
    try:
        return arg1[-1]
    except IndexError:
        return None


def rest_(arg1):
    return arg1[1:]


def pop_(arg1):
    return tuple(arg1[1:])


def nth_(arg1, n):
    try:
        return arg1[n]
    except IndexError:
        return None


def map_(arg1, arg2):
    return tuple(map(arg1, arg2))
