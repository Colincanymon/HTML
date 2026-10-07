num=list(map(int,input('enter the number:').split()))
found=False
for i in num:
    if i>100:
        print(i)
        found=True
    if not found:
        print("over")