def if_(arg1, arg2, arg3=None):
    return arg2 if arg1 else arg3


def gt_(*args):
    return reduce(lambda a, b: a > b, args)


def lt_(*args):
    return reduce(lambda a, b: a < b, args)


def eq_(*args):
    return reduce(lambda a, b: a == b, args)


def add_(*args):
    return reduce(lambda a, b: a + b, args)


def sub_(*args):
    return reduce(lambda a, b: a - b, args)


def mul_(*args):
    return reduce(lambda a, b: a * b, args)


def print_(*args):
    print ' '.join([str(a) for a in args])
