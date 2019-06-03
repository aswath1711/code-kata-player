d=int(input())
n=input().split()
c="kabali"
#print(n)
count=0
    
for i in n:
    if sorted(i)==sorted(c):
        count=count+1
print(count)
