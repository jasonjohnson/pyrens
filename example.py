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
""",
"""
    (defun power (arg1 arg2 arg3)
        (if (> (* arg1 arg2 arg3) 20)
            100
            200))
"""
]

for i, example in enumerate(examples):
    print
    print "Example %d" % i

    r = Reader(example).get();           print r
    g = generate(r);                     print g
    c = compile(g, '<string>', 'exec');  print c

    exec(c)

print power(1, 2, 3)
print power(5, 2, 1)
print power(7, 8, 9)

