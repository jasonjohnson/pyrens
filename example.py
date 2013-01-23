from pyrens.runtime import *
from pyrens.reader import Reader

examples = [
"""
    (if (> 2 (+ 9 7))
        (+ 1 1)
        700)
""",
"""
    (print 1 2 3 4 5)
"""
]

for i, example in enumerate(examples):
    print
    print "Example %d" % i

    r = Reader(example).get(); print r
    g = generate(r);           print g
    e = eval(g);               print e

