l1=input("enter values(comma seperated):")
l1=[int(x) for x in l1.split(",")]
#l1=list(l1)
l2=input("enter values(comma seperated):")
l2=[int(x) for x in l2.split(",")] 
#l2=list(l2)
if len(l1)==len(l2):
	print("same length")
else:
	print("diff length")
if sum(l1)==sum(l2):
	print("sum are same")
else:
	print("not same")
c=[x for x in l1 if x in l2]
if(c):
	print("common are",c)
else:
	print("no common")
