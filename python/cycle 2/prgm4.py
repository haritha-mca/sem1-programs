x=[]
n=int(input("enter the no of elements in list="))
for i in range(0,n):
	a=int(input("enter the value:"))
	if a<=100:
		x.append(a)
	else:
		x.append("over")
print(x)

