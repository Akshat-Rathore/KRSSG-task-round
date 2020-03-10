import socket
import pickle
import threading

HEADERSIZE=10

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

def sumit(clientsocket,tosum):
    msg=pickle.dumps(tosum)
    msg=bytes(f"{len(msg):<{HEADERSIZE}}","utf-8") + msg
    clientsocket.send(msg)
    num=clientsocket.recv(1024)
    num=int(num.decode("utf-8"))
    return num

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1238))
s.listen(1)

clientocket,address=s.accept()


full_msg = b''
new_msg = True
while True:
    msg = clientocket.recv(16)
    if new_msg:
        msglen = int(msg[:HEADERSIZE].decode("utf-8"))
        new_msg = False

    full_msg += msg

    if len(full_msg)-HEADERSIZE == msglen:
        array=(pickle.loads(full_msg[HEADERSIZE:]))
        break

mini=array.pop()

s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.bind((socket.gethostname(),1234))
s1.listen(int(mini)+1)

sum1=0
minions=[]
splitlist=chunkIt(array,int(mini))

for _ in range(int(mini)):
    clientsocket,address=s1.accept()
    minions.append(clientsocket)

for i in range(int(mini)):
    sum1+=sumit(minions[i],splitlist[i])

clientocket.send(bytes(str(sum1),"utf-8"))
