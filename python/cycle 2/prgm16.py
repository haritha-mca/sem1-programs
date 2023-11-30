l1=input("enter values(comma seperated):")
l1=[int(x) for x in l1.split(",")]
p_list=[x for x in l1 if x>0]
print("list contains only positive no:",p_list)
 
sq_list=[x**2 for x in l1]
print("square list contains square of entered list:",sq_list)

str=input("enter a string")
v=[x for x in str if x in 'AaEeIiOoUU']
print("vowels in string:",v)

o=[ord(x) for x in str]
print("ASCII values of each char in string ", str," is",o)

