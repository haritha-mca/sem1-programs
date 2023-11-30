list=input("enter the values:").split(',')
list=[int(item) for item in list]
remove=[i for i in list if i%2!=0]
print("original list:",list)
print("new list without even no:",remove)

