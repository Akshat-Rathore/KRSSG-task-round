import socket
import sys
import select
import time
import schedule     #TO TIME THE LIFT WORLD
import threading
old1=[]    #to maintain data of last visited floor lift 1 for repairing purposes!
old2=[]	   #to maintain data of last visited floor lift 2 for repairing purposes!
PORT=1038
class Lift:
	
	def __init__(self,fl,state,trg):
		self.fl = fl     #present floor of the lift
		self.state = states    #there are  3 states for the lift:U(Moving Upward),I(Idle)and D(Moving Downward)
		self.trg = trg    #target floor

class System():

	def __init__(self,Lift1,Lift2):

		Lift1 = Lift(0,'U',0)   #initially Lift 1 goes upward
		Lift2 = Lift(0,'D',0)   #initially Lift 2 goes Downward

	def transition(self,Lift1,x):	#transition from 1 state to another
		if(Lift1.state=='I'):		#if lift is idle
			if(Lift1.fl<Lift1.trg):
				old1.append(Lift1.fl)
				Lift1.fl+=1
				return('U')
			if(Lift1.fl>Lift1.trg):
				old1.append(Lift1.fl)
				Lift1.fl-=1
				return('D')
			if(Lift1.fl==Lift1.trg):
				old1.append(Lift1.fl)
				return('I')
		elif(Lift1.state=='U'):		#if lift goes up
			if(Lift1.fl<Lift1.trg):
				old1.append(Lift1.fl)
				Lift1.fl+=1
				return('U')
			if(Lift1.fl>Lift1.trg):
				old1.append(Lift1.fl)
				Lift1.fl+=1
				return('U')
			if(Lift1.fl==Lift1.trg):
				if(x==1):
					print("Lift {} -> {}".format(x,str(Lift1.fl)))
				else:
					print("Lift {} -> {}".format(x,str(Lift1.fl))) 
				return('I')
		else:				#if lift goes down
			if(Lift1.fl<Lift1.trg):
				old1.append(Lift1.fl)
				Lift1.fl-=1
				return('D')
			if(Lift1.fl>Lift1.trg):
				old1.append(Lift1.fl)
				Lift1.fl-=1
				return('D')
			if(Lift1.fl==Lift1.trg):
				if(x==2):
					print("Lift {}  ->  {}".format(x,str(Lift1.fl)))
				else:
					print("Lift {}  ->  {}".format(x,str(Lift1.fl))) 
				return('I')

def main():
	liftup = Lift(0,'U',0)
	liftdown = Lift(0,'D',0)
	syss = System(liftup,liftdown)    #defining our lift world
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.bind((socket.gethostname(),PORT))
	server.listen(2)        #COZ ONLY 1 CLIENT SOCKET TO HEAR
	print("Listening")
	HEADERSIZE = 10
	lis = []
	def change(liftup,liftdown):
		if(((liftup.state!='I')and(liftdown.state!='I'))or(len(lis)==0)):    #NOTHING TO CHANGE
			return
		else:
			if((liftup.state=='I')and(len(listup)!=0)):    #LIFT 1 NEEDS TO MOVE
				mi = 100			       #HOPE BUILDING DOES'NT HAVE 100 FLOORS ABOVE TE GROUND
				for i in listup:
					if(i<mi):
						mi = i
				if(mi in listup):
					listup.remove(mi)
				liftup.trg = mi
				liftup.state = 'I'
			if((liftdown.state=='I')and(len(listdown)!=0)):	  # #LIFT 2 NEEDS TO MOVE
				ma = -100									
				for i in listdown:
					if(i>ma):
						ma = i
				if(ma in listdown):
					listdown.remove(ma)
				liftdown.trg = ma
				liftdown.state = 'I'
				return
	def repeat():
		while True:
			liftup.state = syss.transition(liftup,1)
			liftdown.state = syss.transition(liftdown,2)
			change(liftup,liftdown)
			time.sleep(1)

	t1 = threading.Thread(trg = lambda:repeat())
	t1.start()
		
	listup = []
	listdown = []
	conn,addr = server.accept()
	while True:

		msg = conn.recv(HEADERSIZE)
		length  = int(msg.decode("utf-8"))
		full_msg = ""
		while(len(full_msg)!=length):
			part = conn.recv(1).decode("utf-8")
			full_msg += part
		print("Given Input:")
		print(full_msg)

		if(full_msg=="out"):					
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





