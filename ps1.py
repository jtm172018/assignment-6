###### Assignment 1 parity check and framing .py file ###########

####### write your code here ##########

def parity(x):        # function for parity bit
	z=x.count('1')
	if z%2==1:
		return 0
	else:
		return 1

x= input()
x=str(x)
z=parity(x)
z=str(z)
frame=(x+z)
print(frame)    #frame after parity bit addition

m=frame.replace('010','0100')  #bit stuffing
u=m[-2:]   #for accessing last 2 character
d='01'
d=str(d)
if u == d:
	m=m+'0'

final= m+'0101'    #modified string received at other end  
print(final)

	




