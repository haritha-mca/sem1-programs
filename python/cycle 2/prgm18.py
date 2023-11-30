dict1={}
dict2={}
for i in range(3):
        name=input("enter name")
        age=input("enter age")
        dict1[name]=age
for i in range(3):
        place=input("enter place")
        dis=input("enter distance")
        dict2[place]=dis
dict1.update(dict2)
print(dict1)


