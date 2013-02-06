class HashMaps(object):

    def __init__(self, writer):
        self.writer = writer
        self.symbols = {
            'hash-map': '_hash_map',
            'get': '_get',
            'merge': '_merge'
        }

    def _hash_map(self, head, tail):
        """(hash-map "key1" 123 "key2" 456)"""
        length = len(tail)
        collections = ','.join(self.writer.generate_all(tail))

        return 'dict([%s][i:i+2] for i in range(0,%d,2))' % (collections,
                                                             length)

    def _get(self, head, tail):
        """(get my-hash-map "key1")"""
        collection = tail[0]
        key = tail[1]

        return '%s[%s]' % (self.writer.generate(collection),
                           self.writer.generate(key))

    def _merge(self, head, tail):
        """(merge my-hash-map-1 my-hash-map-2)"""
        return 'dict(reduce(lambda a, b: a.items() + b.items(), (%s,)))' % \
            ','.join(self.writer.generate_all(tail))
