from pyrens.runtime import *
import requests
def _fn_1_1(url): return requests.get(url)
fetch = _fn_1_1
print_(fetch("http://www.google.com/"))
