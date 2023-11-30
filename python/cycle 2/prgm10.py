color_list1=[]
color_list2=[]
l1=int(input("enter length of list1:"))
for i in range(0,l1):
	x=input("enter a ele:")
	color_list1.append(x)
l2=int(input("enter length of list2:"))
for i in range(0,l2):
        x=input("enter a ele:")
        color_list2.append(x)
color_list1=[item for item in color_list1]
colorlist1=[item for item in color_list2]
result=[item for item  in color_list1 if item not in color_list2]
print("ele from list1 not in list2:",result)

