from pyrens.runtime import *
x = _add(1,2,3,4,5)
y = _add(1,2,3,4,5)
z = _add(1,2,3,4,5)
def _fn_3_1(arg1,arg2,arg3): return _mul(arg1,arg2,arg3)
func1 = _fn_3_1
def _fn_4_1(arg1,arg2): return _add(arg1,arg2)
func2 = _fn_4_1
def _fn_5_1(arg1): return arg1
func3 = _fn_5_1
def _fn_6_1(): return _print(1)
func4 = _fn_6_1
_print(func1(x,y,z))
_print(func2(x,y))
_print(func3(x))
_print("Hello!")
_print("Hello Lisp World!")
func4()
