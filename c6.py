import socket
import pickle
import time

HEADERSIZE=10

arr=[int(x) for x in input("Enter the numbers: ").split()]
arr.append((input("Enter the Number of Minions you want to connect: ")))
msg=pickle.dumps(arr)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))


msg=bytes(f"{len(msg):<{HEADERSIZE}}","utf-8") + msg
s.send(msg)

new_msg=True
full_msg=b''
sumi=0
    
while True:
    sumi=s.recv(1024)
    sumi=sumi.decode("utf-8")
    break

print(f"The sum is {sumi}")
