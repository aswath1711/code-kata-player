n,k=[int(x) for x in input().split()]
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i in l2:
    l1.append(i)
    l1.sort()
    print(l1[-1],end=" ")
