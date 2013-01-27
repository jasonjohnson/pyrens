from pyrens.reader import Reader
from pyrens.writer import Writer

class Outfile(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.expressions = []
        self.imports = [
            "from pyrens.runtime import *"
        ]

    def load(self, expressions):
        self.expressions = expressions

    def write(self):
        with open(self.file_name, 'w') as outfile:
            seed = 0

            for imp in self.imports:
                outfile.write(imp)
                outfile.write("\n")

            for exp in self.expressions:
                w = Writer(Reader(exp).get(), seed)

                for func in w.get_functions():
                    outfile.write(func)
                    outfile.write("\n")

                outfile.write(w.get())
                outfile.write("\n")

                seed += 1

