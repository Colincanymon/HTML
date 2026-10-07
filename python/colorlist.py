list1=set(["blue","red","green","orange","yellow"])
list2=set(["yellow","blue","black"])
difference=[]
for color in list1:
    if color not in list2:
     difference.append(color)
print(difference)