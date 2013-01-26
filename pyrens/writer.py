class Writer(object):
    def __init__(self, exp):
        self.exp = exp
        self.result = ""
        self.mangled = 0
        self.mangled_names = []
        self.functions = []

    def get(self):
        if not self.result:
            self.result = self.generate()

        return self.result

    def get_functions(self):
        if not self.result:
            self.get()

        return self.functions

    def generate(self, exp=None, bindings=None):
        if not exp:
            exp = self.exp

        if not bindings:
            bindings = []

        generator = self._generic
        generators = {
            'fn': self._fn,
            'let': self._let,
            'def': self._def
        }

        head = exp[0]
        tail = exp[1:]

        if head in generators:
            generator = generators[head]

        if bindings:
            return generator(head, tail, bindings)

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

        if symbol in symbols:
            return symbols[symbol]

        return None

    def complex(self, exp):
        return any([isinstance(e, list) for e in exp])

    def mangle(self):
        self.mangled += 1
        self.mangled_names.append('_fn_%d' % self.mangled)
        return self.mangled_names[-1]

    def function(self, name='', args='', body=''):
        self.functions.append('def %s(%s): %s' % (name, args, body))

    def _let(self, head, tail):
        mangle = self.mangle()

        let = []
        mangled = []
        bindings = tail[0]

        for binding in bindings:
            name = binding[0]
            value = binding[1:]
            value = value.pop() if self.complex(value) else value
            value = self.generate(value)

            if value in self.mangled_names:
                mangled.append(name)

            let.append('%s = %s' % (name, value))

        self.function(mangle, '', '%s; return %s' % \
                (';'.join(let), self.generate(tail[1], bindings=mangled)))

        return '%s()' % mangle

    def _def(self, head, tail):
        name = tail[0]
        body = self.generate(tail[1])

        return '%s = %s' % (name, body)

    def _fn(self, head, tail):
        mangle = self.mangle()

        args = tail[0]
        body = self.generate(tail[1])

        self.function(mangle, ','.join(args), 'return %s' % body)

        return mangle

    def _generic(self, head, tail, bindings=None):
        if not bindings:
            bindings = []

        for i, e in enumerate(tail):
            if isinstance(e, list):
                tail[i] = self.generate(e, bindings)

        if head in bindings:
            symbol = head
        else:
            symbol = self.resolve(head)

        if not symbol:
            return self._raw(head, tail)

        return '%s(%s)' % (symbol, ','.join(tail))

    def _raw(self, head, tail=None):
        if not tail:
            tail = []

        return ' '.join([head] + tail)
