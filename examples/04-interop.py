from functools import partial
import socket
import requests
def _fn_1_1(url): return requests.get(url)
fetch = _fn_1_1
print fetch("http://www.google.com/");
