lst=[]
l=int(input("enter length of list1:"))
for i in range(0,l):
	x=input("enter a ele:")
	lst.append(x)
lst=[item for item in lst]
print("first color:",lst[0])
print("second color:",lst[-1])

