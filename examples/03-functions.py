def _fn_0_1(arg1,arg2,arg3): return 100 if reduce(lambda a, b: a > b, (reduce(lambda a, b: a * b, (arg1,arg2,arg3,)),20,)) else 200
power = _fn_0_1
print power(1,2,3);
