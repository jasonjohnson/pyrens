class Infile(object):
    SCAN = 1
    CONSUME = 1

    def __init__(self, file_name):
        self.file_name = file_name
        self.positions = []
        self.state = Infile.SCAN

    def scan(self):
        position = 0
        depth = 0
        start = None
        end = None

        with open(self.file_name) as infile:
            while True:
                char = infile.read(1)
                if not char:
                    break

                if char == ')':
                    depth -= 1

                if all([self.state == Infile.SCAN,
                        depth == 0,
                        char == '(']):
                    start = position
                    self.state = Infile.CONSUME

                if all([self.state == Infile.CONSUME,
                        depth == 0,
                        char == ')']):
                    end = position
                    self.state = Infile.SCAN

                if start is not None and end is not None:
                    self.positions.append((start, end))
                    start = None
                    end = None

                if char == '(':
                    depth += 1

                position += 1

    def expressions(self):
        exps = []

        with open(self.file_name) as infile:
            for start, end in self.positions:
                size = (end + 1) - start
                infile.seek(start)
                exps.append(infile.read(size))

        return exps
