from functools import partial
import socket
sock = socket.socket()
sock.connect(("google.com",80))
def _fn_2_1(verb,path): return str("".join((verb," ",path," HTTP/1.1\r\n\r\n",)))
http_request = _fn_2_1
sock.send(http_request("GET","/"))
print sock.recv(1024);
sock.close()
