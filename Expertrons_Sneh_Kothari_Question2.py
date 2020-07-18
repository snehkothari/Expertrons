list1=[]
size1=int(input("Enter size of list 1"))

for i in range(0,size1):
	list1.append(input("Enter element"))

list2=[]
size2=int(input("Enter size of list 2"))

for i in range(0,size2):
	list2.append(input("Enter element"))

final_list1=[]
for item in list1:
	if item in list2:
		list2.remove(item)
	else:
		final_list1.append(item)

print(final_list1+list2)