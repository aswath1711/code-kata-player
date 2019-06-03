d=int(input())
n=[]
for i in range(d):
    str=input()
    n.append(str)
c="kabali"
#print(n)
count=0
    
for i in n:
    if sorted(i)==sorted(c):
        count=count+1
print(count)
