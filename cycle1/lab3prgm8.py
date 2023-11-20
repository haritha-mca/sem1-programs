n=int(input("enter a positive integer:"))
if n>0:
	rev=0
	while n>0:
		rev=(rev*10)+(n%10)
		n=n//10
print(rev)

