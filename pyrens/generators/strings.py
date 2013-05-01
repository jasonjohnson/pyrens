class Strings(object):

    def __init__(self, writer):
        self.writer = writer
        self.symbols = {
            'str': '_str',
            'strip': '_strip'
        }

    def _str(self, head, tail):
        return 'str("".join(map(str,(%s,))))' % \
            ','.join(self.writer.generate_all(tail))

    def _strip(self, head, tail):
        string = self.writer.generate(tail[0])

        return '%s.strip()' % string
