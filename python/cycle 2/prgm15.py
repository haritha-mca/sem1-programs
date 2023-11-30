words=input("enter list of words seperated by space:").split()
max=0
for word in words:
	if len(word)>max:
		max=len(word)
print("the length of the longest word:",max)

