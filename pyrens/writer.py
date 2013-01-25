class Writer(object):
    def __init__(self, exp):
        self.exp = exp

    def get(self):
        return self.generate()

    def generate(self):
        generator = None
        generators = {
            'let': self._let,
            'defun': self._defun
        }

        head = self.exp[0]
        tail = self.exp[1:]

        if head in generators:
            generator = generators[head]
        else:
            generator = self._generic

        return generator(head, tail)

    def resolve(self, symbol):
        symbols = {
            '>': '_gt',
            '<': '_lt',
            '=': '_eq',
            '+': '_add',
            '-': '_sub',
            '*': '_mul',
            'if': '_if',
            'print': '_print'
        }

        return symbols[symbol]

    def complex(self):
        return any([isinstance(e, list) for e in self.exp])

    def _let(self, head, tail):
        pass

    def _defun(self, head, tail):
        name = tail[0]
        args = tail[1]
        body = Writer(tail[2]).get()

        return 'def %s(%s): return %s' % (name, ','.join(args), body)

    def _generic(self, head, tail):
        for i, e in enumerate(tail):
            if isinstance(e, list):
                tail[i] = Writer(e).get()

        return '%s(%s)' % (self.resolve(head), ','.join(tail))

