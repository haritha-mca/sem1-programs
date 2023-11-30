txt=input("enter line of text:")
words=txt.split(" ")
c={}
for t in words:
	if t in c:
		c[t]+=1
	else:
		c[t]=1
print(c)

