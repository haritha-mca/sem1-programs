name=input("enter a list of first names(comma-seperated):")
first_name=name.split(',')
occurance=[name.lower().count('a') for name in first_name]
for i in range(len(first_name)):
	print(f"{first_name[i]}:{occurance[1]} occurance of 'a'")
