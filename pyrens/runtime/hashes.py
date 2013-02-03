def hash_(*args):
    return dict(args[i:i+2] for i in range(0, len(args), 2))


def get_(arg1, arg2):
    try:
        return arg1[arg2]
    except KeyError:
        return None


def merge_(*args):
    return dict(reduce(lambda a, b: a.items() + b.items(), args))
