from pyrens.runtime import *
from pyrens.reader import Reader
from pyrens.writer import Writer

files = ['examples/ex1.lisp', 'examples/ex2.lisp', 'examples/ex3.lisp']

# Generate .py files for each .lisp input file
for f in files:
    with open(f, 'r') as infile:
        with open(f.replace('lisp', 'py'), 'w') as outfile:
            print
            print "Processing: %s" % f

            e = infile.read().strip()
            print e

            r = Reader(e).get()
            print r

            w = Writer(r).get()
            print w

            outfile.write(w)

