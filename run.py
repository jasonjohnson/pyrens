from glob import glob
from pyrens.reader import Reader
from pyrens.writer import Writer

files = glob('examples/*.lisp')
files.sort()

for f in files:
    with open(f, 'r') as infile:
        with open(f.replace('lisp', 'py'), 'w') as outfile:
            print
            print "Processing: %s" % f

            i = infile.read().strip()
            print i

            r = Reader(i).get()
            print r

            w = Writer(r)
            print w.get_functions()
            print w.get()

            outfile.write("from pyrens.runtime import *")
            outfile.write("\n")

            for func in w.get_functions():
                outfile.write(func)
                outfile.write("\n")

            outfile.write(w.get())

