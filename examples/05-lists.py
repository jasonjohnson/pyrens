from functools import partial
import socket
mylist = (1,2,3,4,5,)
mylist2 = (6,)
mylist3 = (7,reduce(lambda a, b: a + b, (7,1,)),)
mystrings = ("Pyrens","is","awesome!",)
def _fn_4_1(i): return reduce(lambda a, b: a + b, (5,i,))
plus5 = _fn_4_1
def _fn_5_1(s): return len(s)
counter = _fn_5_1
print "List: ", mylist;
print "My Strings: ", mystrings;
print mylist[0];
print mylist[1];
print mylist[2];
print mylist[3];
print mylist[4];
print "Count: ", len(mylist);
print "First: ", mylist[0];
print "Last: ", mylist[-1];
print "Rest: ", mylist[1:];
print "Pop: ", tuple(mylist[1:]);
print map(plus5, mylist);
mylenghts = map(counter, mystrings)
print mylenghts[0];
print mylenghts[1:];
print mylist2;
print (5,) + mylist2;
