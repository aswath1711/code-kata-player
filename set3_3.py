n,k=[int(x) for x in input().split()]
a=list(map(int,input().split()))
ad=list(map(int,input().split()))
for i in ad:
    a.append(i)
    a.sort()
    print(a[-1],end=" ")