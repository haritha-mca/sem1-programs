n=int(input("enter no of terms:"))
a=0
b=1
if n<=0:
	print("the output is:",a)
else:
	print(a,b,end="")
for x in range(2,n):
	c=a+b
	print(c,end="")
	a=b
	b=c
