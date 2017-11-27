import socket
from struct import pack

s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = pack("I", 0xFBA2)
s.connect(("127.0.0.1", 2222))
s.send(data)