from pyrens.runtime import *
mylist = list_(1,2,3,4,5)
mylist2 = list_(6)
mystrings = list_("Pyrens","is","awesome!")
def _fn_3_1(i): return add_(5,i)
plus5 = _fn_3_1
def _fn_4_1(s): return count_(s)
counter = _fn_4_1
print_("List: ",mylist)
print_(nth_(mylist,0))
print_(nth_(mylist,1))
print_(nth_(mylist,2))
print_(nth_(mylist,3))
print_(nth_(mylist,4))
print_(nth_(mylist,5))
print_("Count: ",count_(mylist))
print_("First: ",first_(mylist))
print_("Last: ",last_(mylist))
print_("Rest: ",rest_(mylist))
print_("Pop: ",pop_(mylist))
print_(map_(plus5,mylist))
mylenghts = map_(counter,mystrings)
print_(first_(mylenghts))
print_(rest_(mylenghts))
print_(mylist2)
print_(cons_(5,mylist2))
