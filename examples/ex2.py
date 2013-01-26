from pyrens.runtime import *
def _fn_3(a1,a2): return _add(a1,a2)
def _fn_2(): a = _fn_3;b = _mul(72,8,2);c = 3; return _mul(a(2,2),b,c)
def _fn_1(x,y,z): return _mul(_fn_2(),x,y,z)
testing = _fn_1