x1,y1=[int(i) for i in input().split()]
x2,y2=[int(i) for i in input().split()]
x3,y3=[int(i) for i in input().split()]

slope= x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) 
if slope==0:
    print("yes")
else:
    print("no")