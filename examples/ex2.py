from pyrens.runtime import *
def _fn_0_3(a1,a2): return _add(a1,a2)
def _fn_0_2(____s): exec(""); locals().update(____s); a = _fn_0_3;b = _mul(72,8,2);c = 3456; return _mul(a(2,2),b,c)
def _fn_0_1(x,y,z): return _mul(_fn_0_2(locals()),x,y,z)
testing = _fn_0_1
_print(testing(1,2,3))
def _fn_2_2(____s): exec(""); locals().update(____s); c = 3; return _add(a,b,c)
def _fn_2_1(a,b): return _fn_2_2(locals())
scope = _fn_2_1
_print(scope(1,2))
