from functools import partial
import socket
s = "abc"
i = 123
my_string = str("".join(map(str,("  ",s,"  ",i,"  ",))))
print my_string;
print my_string.strip();
