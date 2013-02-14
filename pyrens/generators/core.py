class Core(object):

    def __init__(self, writer):
        self.writer = writer
        self.symbols = {
            'def': '_def',
            'if': '_if',
            '>': '_gt',
            '<': '_lt',
            '=': '_eq',
            '+': '_add',
            '-': '_sub',
            '*': '_mul',
            '/': '_div',
            'print': '_print',
            'from': '_from',
            'import': '_import'
        }

    def _def(self, head, tail):
        """(def x 123)"""
        name = tail[0].replace('-', '_')
        body = self.writer.generate(tail[1])

        return '%s = %s' % (name, body)

    def _if(self, head, tail):
        """(if (> 10 20) 100 200)"""
        predicate = self.writer.generate(tail[0])
        consequent = self.writer.generate(tail[1])
        alternate = self.writer.generate(tail[2]) if len(tail) == 3 else 'None'

        return '%s if %s else %s' % (consequent, predicate, alternate)

    def _gt(self, head, tail):
        """(> 30 20 10)"""
        return 'reduce(lambda a, b: a > b, (%s,))' % \
            ','.join(self.writer.generate_all(tail))

    def _lt(self, head, tail):
        """(< 10 20 30)"""
        return 'reduce(lambda a, b: a < b, (%s,))' % \
            ','.join(self.writer.generate_all(tail))

    def _eq(self, head, tail):
        """(= 10 10 10)"""
        return 'reduce(lambda a, b: a == b, (%s,))' % \
            ','.join(self.writer.generate_all(tail))

    def _add(self, head, tail):
        """(+ 30 20 10)"""
        return 'reduce(lambda a, b: a + b, (%s,))' % \
            ','.join(self.writer.generate_all(tail))

    def _sub(self, head, tail):
        """(- 30 20 10)"""
        return 'reduce(lambda a, b: a - b, (%s,))' % \
            ','.join(self.writer.generate_all(tail))

    def _mul(self, head, tail):
        """(* 30 20 10)"""
        return 'reduce(lambda a, b: a * b, (%s,))' % \
            ','.join(self.writer.generate_all(tail))

    def _div(self, head, tail):
        """(/ 30 20 10)"""
        return 'reduce(lambda a, b: a / b, (%s,))' % \
            ','.join(self.writer.generate_all(tail))

    def _print(self, head, tail):
        """(print 1 2 3 4 my-list "Hello World!")"""
        return 'print %s;' % \
            ', '.join([str(a) for a in self.writer.generate_all(tail)])

    def _from(self, head, tail):
        """(from module import function)"""
        lib = tail[0]
        items = tail[1:]

        return 'from %s import %s' % (lib, ','.join(items))

    def _import(self, head, tail):
        """(import module.submodule)"""
        lib = tail[0]

        return 'import %s' % lib
