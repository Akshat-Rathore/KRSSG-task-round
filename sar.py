import socket
import sys
import select
import time
import schedule
import threading
old1=[]
old2=[]
class Lift:
	
	def __init__(self,floor,state,target):
		self.floor = floor
		self.state = state
		self.target = target

class System():

	def __init__(self,Lift1,Lift2):

		Lift1 = Lift(0,'U',0)
		Lift2 = Lift(0,'D',0)

	def transition(self,Lift1,x):
		if(Lift1.state=='I'):
			if(Lift1.floor<Lift1.target):
				old1.append(Lift1.floor)
				Lift1.floor+=1
				return('U')
			if(Lift1.floor>Lift1.target):
				Lift1.floor-=1
				return('D')
			if(Lift1.floor==Lift1.target):
				return('I')
		elif(Lift1.state=='U'):
			if(Lift1.floor<Lift1.target):
				Lift1.floor+=1
				return('U')
			if(Lift1.floor>Lift1.target):
				Lift1.floor+=1
				return('U')
			if(Lift1.floor==Lift1.target):
				if(x==1):
					print("Lift {} reached floor {}".format(x,str(Lift1.floor)))
				else:
					print("Lift {} reached floor {}".format(x,str(Lift1.floor))) 
				return('I')
		else:
			if(Lift1.floor<Lift1.target):
				Lift1.floor-=1
				return('D')
			if(Lift1.floor>Lift1.target):
				Lift1.floor-=1
				return('D')
			if(Lift1.floor==Lift1.target):
				if(x==2):
					print("Lift {}  ->  {}".format(x,str(Lift1.floor)))
				else:
					print("Lift {}  ->  {}".format(x,str(Lift1.floor))) 
				return('I')

def main():
	liftup = Lift(0,'U',0)
	liftdown = Lift(0,'D',0)
	syss = System(liftup,liftdown)
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.bind((socket.gethostname(),1038))
	server.listen(2)
	print("Listening")
	head_size = 10
	lis = []
	def change(liftup,liftdown):
		if(((liftup.state!='I')and(liftdown.state!='I'))or(len(lis)==0)):
			return
		else:
			if((liftup.state=='I')and(len(listup)!=0)):
				mi = 100
				for ele in listup:
					if(ele<mi):
						mi = ele
				if(mi in listup):
					listup.remove(mi)
				liftup.target = mi
				liftup.state = 'I'
			if((liftdown.state=='I')and(len(listdown)!=0)):
				ma = -100
				for ele in listdown:
					if(ele>ma):
						ma = ele
				if(ma in listdown):
					listdown.remove(ma)
				liftdown.target = ma
				liftdown.state = 'I'
				return
	def repeat():
		while True:
			liftup.state = syss.transition(liftup,1)
			liftdown.state = syss.transition(liftdown,2)
			change(liftup,liftdown)
			time.sleep(1)

	t1 = threading.Thread(target = lambda:repeat())
	t1.start()
		
	listup = []
	listdown = []
	conn,addr = server.accept()
	while True:

		msg = conn.recv(head_size)
		length  = int(msg.decode("utf-8"))
		full_msg = ""
		while(len(full_msg)!=length):
			part = conn.recv(1).decode("utf-8")
			full_msg += part
		print(full_msg)

		if(full_msg=="exit"):
			exit()			
			break
		else:
			lis.append(full_msg)
			li = full_msg.split(' ')
			if(li[1]=='U'):
				listup.append(int(li[0]))
				listup.append(int(li[2]))
			if(li[1]=='D'):
				listdown.append(int(li[0]))
				listdown.append(int(li[2]))
if __name__ =="__main__":
	main()


