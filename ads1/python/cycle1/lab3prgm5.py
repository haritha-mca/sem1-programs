n=int(input("enter a positive number:"))
if n>0:
	for i in range(1,11):
		print(n,"x",i,"=",n*i)
else:
	print("invalid input")
