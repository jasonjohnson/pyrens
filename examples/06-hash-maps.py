from functools import partial
import socket
myhash1 = dict(["key1",(1,2,3,),"key2",2][i:i+2] for i in range(0,4,2))
myhash2 = dict(["key3",3][i:i+2] for i in range(0,2,2))
myhash3 = dict(reduce(lambda a, b: a.items() + b.items(), (myhash1,myhash2,)))
print myhash1["key1"];
print myhash1["key2"];
print myhash2;
print myhash3;
print myhash3["key1"][0];
print len(myhash3);
