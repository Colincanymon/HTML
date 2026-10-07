list=[1,2,3,4,5,6]
print(list)
n=int(input("enter the value to add:"))
list.append(n)
p=int(input("enter the value to remove:"))
if p in list:
    list.remove(p)
    print("the number",p,"is removed from the list")
else:
    print("the number",p,"is not in the list")
print(list)