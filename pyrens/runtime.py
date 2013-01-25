__all__ = [
    '_if', '_gt', '_lt', '_eq', '_add', '_sub', '_mul', '_print'
]

def _if(arg1, arg2, arg3):
    return arg2 if arg1 else arg3

def _gt(*args):
    return reduce(lambda a, b: a > b, args)

def _lt(*args):
    return reduce(lambda a, b: a < b, args)

def _eq(*args):
    return reduce(lambda a, b: a == b, args)

def _add(*args):
    return reduce(lambda a, b: a + b, args)

def _sub(*args):
    return reduce(lambda a, b: a - b, args)

def _mul(*args):
    return reduce(lambda a, b: a * b, args)

def _print(*args):
    print ' '.join([str(a) for a in args])

