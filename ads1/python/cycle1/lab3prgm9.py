n=int(input("enter a number:"))
sum=0
temp=n
while temp>0:
	digit=temp%10
	sum+=digit**3
	temp//=10
if n==sum:
	print("no is armstrong",n)
else:
	print("no is not armstrong",n)
