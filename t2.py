
class Lift:
    st=0
    def __init__(self):
       self.cf=0
       self.d=0
       self.direc=0

class sys(Lift):

    def __init__(self,lift1,lift2):
        self.lift1=lift1
        self.lift2=lift2

    def progress(self):
        self.lift1.cf+=self.lift1.st
        self.lift2.cf+=self.lift2.st

    def get_state(self,var):
        if var==lift1:
            var=self.lift1
        else:
             var=self.lift2
        if var.st==1:
            return 'U'
        elif var.st==-1:
            return 'D'
        else :
            return 'S'

    
    def change_state(self,var):
        if var==lift1:
            var=self.lift1
        else:
             var=self.lift2
        var.st=-var.st
    
    def stop(self,var):
        if var==lift1:
            var=self.lift1
        else:
             var=self.lift2
            
        var.st=0

    def update_dest(self,var,new):
        if var==lift1:
            var=self.lift1
        else:
             var=self.lift2
        
        if (var.direc)*(var.d) < (var.direc)*new:
            var.d=new

    

def mf(x):
  return list(dict.fromkeys(x))

def bs(arr):
    n = len(arr)
 
    for i in range(n):
 
        for j in range(0, n-i-1):
            if abs(int(float(arr[j][0]))) > abs(int(float(arr[j+1][0]))) :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bs2(arr):
    n = len(arr)
 
    for i in range(n):
 
        for j in range(0, n-i-1):
            if abs(int(float(arr[j]))) < abs(int(float(arr[j+1]))) :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bs3(arr):
    n = len(arr)
 
    for i in range(n):
 
        for j in range(0, n-i-1):
            if abs(int(float(arr[j]))) > abs(int(float(arr[j+1]))) :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bs5(arr):
    n = len(arr)
 
    for i in range(n):
 
        for j in range(0, n-i-1):
 
            if arr[j][0] < arr[j+1][0] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
def bs1(arr):
    n = len(arr)
 
    for i in range(n):
 
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bs31(arr):
    n = len(arr)
 
    for i in range(n):
 
        for j in range(0, n-i-1):
 
            if arr[j] < arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def ca(a,b):
    i=0
    while i <len(a):
        
        if a[i]>b:
            j=len(a)-1
            a.append(a[j])
            while j+1>=i:
                a[j+1]=a[j]
            a[i]=b
            breaks
        i+=1
        print(a)
    return (a)
def caa(a,b):
    i=0
    while i <len(a):
        
        if a[i]>b:
            j=len(a)-1
            a.append(a[j])
            while j+1>=i:
                a[j+1]=a[j]
            a[i]=b
            breaks
        i+=1
        print(a)
    return (a)


n=int(input("Enter the Number of Passengers:"))

pd1=[]
pd2=[]

for _ in range(n):
    temp1=input()
    temp=temp1.split()
    if int(temp[0]) < 0 or int(temp[2])<0:
        pd1.append(temp)
    else:
        pd2.append(temp)

bs(pd1)
bs(pd2)

print(pd1)
print(pd2)

i=0
max1=0
max2=0
max_1=0
while i < len(pd1):
    if max1>int(pd1[i][0]):
        max1=int(pd1[i][0])
    if max2>int(pd1[i][2]):
        max2=int(pd1[i][2])
    i+=1
max_1=min(max1,max2)


i=0
max3=0
max4=0
max_2=0
while i < len(pd2):
    if max3<int(pd2[i][0]):
        max3=int(pd2[i][0])
    if max4<int(pd2[i][2]):
        max4=int(pd2[i][2])
    i+=1
max_2=max(max3,max4)

lift1=Lift()
lift2=Lift()
lift1.st=-1
lift2.st=1
old=0
system=sys(lift1,lift2)
count=0
l1d=[]
l1u=[]
l1=[]
l2=[]
i=0
flag=0



#LIFT 1
while len(l1d)+len(l1u) <= len(pd1):
    a=pd1[i]
    if (a[1]=='U' and lift1.st==1 ) or (a[1]=='D' and lift1.st==-1):

        if a[1]=='D':
            l1d.append(a[0])             
            l1d.append(a[2])
            # print(l1d)
        if a[1]=='U':
            l1u.append(a[0])
            l1u.append(a[2])
            # print(l1u)
    
        
    if i<len(pd1)-1 and flag==0:
        i+=1
    
    else:
        flag+=1
        
        if flag==1:
            lift1.st=-lift1.st
            
        i-=1




if len(l1d)>0:
    
    l1d=mf(l1d)
    (bs3(l1d))
    l1.append(l1d)
if len(l1u)>0:
    
    l1u=mf(l1u)
    (bs1(l1u))
    l1.append(l1u)


print ("LIFT 1:")
print(l1)







#lift 2

l1d=[]
l1u=[]
i=0
while len(l1d)+len(l1u) <= len(pd2):
    a=pd2[i]
    if (a[1]=='U' and lift2.st==1 ) or (a[1]=='D' and lift2.st==-1):

        if a[1]=='D':
            l1d.append(a[0])             
            l1d.append(a[2])
            print(l1d)
        if a[1]=='U':
            l1u.append(a[0])
            l1u.append(a[2])
            print(l1u)
    
        
    if i<=len(pd2)-1 and flag==0:
        i+=1
   
   
    else:
        
        
        if flag==1:
            lift2.st=-lift2.st
            flag+=1
            
        i-=1

if len((l1u))>0:
    l1u=mf(l1u)
    bs1(l1u)
    l2.append(l1u)
if len(l1d)>0:
    l1d=mf(l1d)
    bs3(l1d)
    l2.append(l1d)



print ("LIFT 2:")
print(l1u)























        





































# while len(pd1)!=0 and len(pd2)!=0 and count<10:
#     if lift1.direc:
#         old=lift1.cf
#         system.progress()
#         print(f"Lift 1: {old}-->{lift1.cf}")
#         if int(pd1[-1][0])==lift1.cf:
#             system.update_dest('lift1',int(pd1[-1][2]))
#             pd1.pop()
#         if lift1.cf==lift1.d:
#             if system.get_state('lift1') == pd1[-1][1]:
#                 system.update_dest('lift1',int(pd1[-1][0]))
#             else:
#                 system.change_state('lift1')
#         if len(pd1)==0:
#             system.stop('lift1')
#         print(pd1)
    
#     if lift2.direc:
#         old=lift2.cf
#         system.progress()
#         print(f"Lift 2: {old}-->{lift2.cf}")
#         if int(pd2[-1][0])==lift2.cf:
#             system.update_dest('lift2',int(pd2[-1][2]))
#             pd2.pop()
#         if lift2.cf==lift2.d:
#             if system.get_state('lift2') == pd2[-1][1]:
#                 system.update_dest('lift2',int(pd2[-1][0]))
#             else:
#                 system.change_state('lift2')
#         if len(pd2)==0:
#             system.stop('lift2')
#         print(pd2)

#     count+=1