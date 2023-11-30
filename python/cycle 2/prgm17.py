mydict={}
for i in range(3):
	name=input("Enter the name:")
	age=input("Enter the age:")
	mydict[name]=age
mykeys=list(mydict.keys())
mykeys.sort()
asce={i:mydict[i] for i in mykeys}
mykeys.sort(reverse=True)
desc={i:mydict[i] for i  in mykeys}
print("ascending order:",asce)
print("descending order :", desc)

