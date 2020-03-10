import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((socket.gethostname(),1038))

print("Enter your inputs : \n")
msg = ""
while(msg!="done"):
	msg = input()
	full_msg = f"{len(msg):<10}"+msg
	client.send(bytes(full_msg.encode("utf-8")))
	
