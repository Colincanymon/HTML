words=list(input('Enter the words:').split())
found=False
for i in set(words):#we use set of removing the duplicates
    if words.count(i)>1:
        print(i ,'occurs',words.count(i),'times')
        found=True
if not found:
    print("words are not repeating")