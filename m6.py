import socket
import pickle

HEADERSIZE=10

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

full_msg = b''
new_msg = True
while True:
    msg = s.recv(16)
    if new_msg:
        msglen = int(msg[:HEADERSIZE].decode("utf-8"))
        new_msg = False

    full_msg += msg

    if len(full_msg)-HEADERSIZE == msglen:
        array=(pickle.loads(full_msg[HEADERSIZE:]))
        break
print(array)
s.send(bytes(str(sum(array)),"utf-8"))