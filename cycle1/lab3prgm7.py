n=int(input("enter a number:"))
if n>0:
	factors=[]
i=1
while i<=n:
	if n%i==0:
		factors.append(i)
		i+=1
		print(factors)
else:
	print("invalid input")
