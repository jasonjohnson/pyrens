class Sockets(object):

    def __init__(self, writer):
        self.writer = writer
        self.symbols = {
            'socket-create': '_socket_create',
            'socket-connect': '_socket_connect',
            'socket-read': '_socket_read',
            'socket-write': '_socket_write',
            'socket-close': '_socket_close'
        }

    def _socket_create(self, head, tail):
        return 'socket.socket()'

    def _socket_connect(self, head, tail):
        socket = self.writer.generate(tail[0])
        host = self.writer.generate(tail[1])
        port = self.writer.generate(tail[2])

        return '%s.connect((%s,%s))' % (socket, host, port)

    def _socket_read(self, head, tail):
        socket = self.writer.generate(tail[0])
        size = self.writer.generate(tail[1]) if len(tail) == 2 else 1024

        return '%s.recv(%s)' % (socket, size)

    def _socket_write(self, head, tail):
        socket = self.writer.generate(tail[0])
        data = self.writer.generate(tail[1])

        return '%s.send(%s)' % (socket, data)

    def _socket_close(self, head, tail):
        socket = self.writer.generate(tail[0])

        return '%s.close()' % socket
