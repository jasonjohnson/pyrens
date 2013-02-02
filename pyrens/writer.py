class Writer(object):

    def __init__(self, exp, seed=0):
        self.exp = exp
        self.result = ""
        self.seed = seed
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

    def generate(self, exp=None, callables=None):
        if not exp:
            exp = self.exp

        if not callables:
            callables = []

        generator = self._generic
        generators = {
            'fn': self._fn,
            'let': self._let,
            'def': self._def,
            'from': self._from,
            'import': self._import
        }

        head = exp[0]
        tail = exp[1:]

        if head in generators:
            generator = generators[head]

        if callables:
            return generator(head, tail, callables)

        return generator(head, tail)

    def resolve(self, symbol, callables):
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

        if symbol in callables:
            return symbol

        return None

    def complex(self, exp):
        return any([isinstance(e, list) for e in exp])

    def mangle(self):
        self.mangled += 1
        self.mangled_names.append('_fn_%d_%d' % (self.seed, self.mangled))
        return self.mangled_names[-1]

    def function(self, name='', args='', body=''):
        self.functions.append('def %s(%s): %s' % (name, args, body))

    def _from(self, head, tail):
        lib = tail[0]
        items = tail[1:]
        return 'from %s import %s' % (lib, ','.join(items))

    def _import(self, head, tail):
        lib = tail[0]
        return 'import %s' % lib

    def _let(self, head, tail):
        mangle = self.mangle()

        let = []
        callables = []

        bindings = tail[0]

        for binding in bindings:
            name = binding[0]
            value = binding[1:]
            value = value.pop() if self.complex(value) else value
            value = self.generate(value)

            if value in self.mangled_names:
                callables.append(name)

            let.append('%s = %s' % (name, value))

        # The empty exec() prevents python from making assumptions about the
        # local scope of the function. This allows our locals() update to work.
        args = '___s'
        body = 'exec(""); locals().update(___s); %s; return %s' % \
               (';'.join(let), self.generate(tail[1], callables=callables))

        self.function(mangle, args, body)

        # Passing in the current locals() state allows variables defined in the
        # current scope to be available inside our let block.
        return '%s(locals())' % mangle

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

    def _generic(self, head, tail, callables=None):
        if not callables:
            callables = []

        for i, e in enumerate(tail):
            if isinstance(e, list):
                tail[i] = self.generate(e, callables)

        symbol = self.resolve(head, callables)

        if not symbol:
            return self._raw(head, tail)

        return '%s(%s)' % (symbol, ','.join(tail))

    def _raw(self, head, tail=None):
        if isinstance(head, str) and isinstance(tail, str):
            return '%s%s' % (head, tail)

        if isinstance(head, str) and isinstance(tail, list):
            if len(tail) > 0 or head[0].isalpha():
                return '%s(%s)' % (head, ','.join(tail))

        return head
