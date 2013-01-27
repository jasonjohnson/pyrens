from glob import glob
from pyrens.io.infile import Infile
from pyrens.io.outfile import Outfile

file_names = glob('examples/*.lisp')
file_names.sort()

for file_name_in in file_names:
    file_name_out = file_name_in.replace('lisp', 'py')

    print "<< Loading... %s" % file_name_in

    infile = Infile(file_name_in)
    infile.scan()

    print ">> Writing... %s" % file_name_out

    outfile = Outfile(file_name_out)
    outfile.load(infile.expressions())
    outfile.write()

