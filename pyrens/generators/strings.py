class Strings(object):

    def __init__(self, writer):
        self.writer = writer
        self.symbols = {
            'str': '_str',
            'trim': '_trim'
        }

    def _str(self, head, tail):
        return 'str("".join((%s,)))' % ','.join(self.writer.generate_all(tail))

    def _trim(self, head, tail):
        string = self.writer.generate(tail[0])

        return '%s.trim()' % string
