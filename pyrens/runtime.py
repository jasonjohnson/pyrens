__all__ = [
    'functions', 'generate',
    '_if', '_gt', '_lt', '_eq', '_add', '_sub', '_mul', '_print'
]

functions = {
    '>': '_gt',
    '<': '_lt',
    '=': '_eq',
    '+': '_add',
    '-': '_sub',
    '*': '_mul',
    'if': '_if',
    'print': '_print'
}

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

def complex(exp):
    return any([isinstance(e, list) for e in exp])

def resolve(symbol):
    if symbol in functions:
        return functions[symbol]

    return symbol

def generate(exp):
    head = exp[0]
    tail = exp[1:]

    if head == 'defun':
        name = tail[0]
        args = tail[1]
        body = generate(tail[2])

        return 'def %s(%s): return %s' % (name, ','.join(args), body)
    else:
        for i, e in enumerate(exp):
            if isinstance(e, list):
                exp[i] = generate(e)

        return '%s(%s)' % (resolve(exp[0]), ','.join(exp[1:]))

