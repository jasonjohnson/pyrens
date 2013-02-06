class Lists(object):

    def __init__(self, writer):
        self.writer = writer
        self.symbols = {
            'list': '_list',
            'count': '_count',
            'cons': '_cons',
            'first': '_first',
            'last': '_last',
            'rest': '_rest',
            'pop': '_pop',
            'nth': '_nth',
            'map': '_map',
        }

    def _list(self, head, tail):
        """(list 1 2 3 4 5 6)"""
        return '(%s,)' % ','.join(self.writer.generate_all(tail))

    def _count(self, head, tail):
        """(count my-list)"""
        collection = tail[0]

        return 'len(%s)' % self.writer.generate(collection)

    def _cons(self, head, tail):
        """(cons 7 my-list)"""
        new = tail[0]
        existing = tail[1]

        return '(%s,) + %s' % (self.writer.generate(new),
                               self.writer.generate(existing))

    def _first(self, head, tail):
        """(first my-list)"""
        collection = tail[0]

        return '%s[0]' % self.writer.generate(collection)

    def _last(self, head, tail):
        """(last my-list)"""
        collection = tail[0]

        return '%s[-1]' % self.writer.generate(collection)

    def _rest(self, head, tail):
        """(rest my-list)"""
        collection = tail[0]

        return '%s[1:]' % self.writer.generate(collection)

    def _pop(self, head, tail):
        """(pop my-list)"""
        collection = tail[0]

        return 'tuple(%s[1:])' % self.writer.generate(collection)

    def _nth(self, head, tail):
        """(nth my-list 12)"""
        collection = tail[0]
        offset = tail[1]

        return '%s[%s]' % (self.writer.generate(collection),
                           self.writer.generate(offset))

    def _map(self, head, tail):
        """(map (fn (i) (+ i 5)) my-list)"""
        function = tail[0]
        collection = tail[1]

        return 'map(%s, %s)' % (self.writer.generate(function),
                                self.writer.generate(collection))
