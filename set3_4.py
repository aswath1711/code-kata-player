n=input()
count=0
for i in n:
    if i.isnumeric():
        continue
    else:
        count=1
        break
if(count==0):
    print("yes")
else:
    print("no")