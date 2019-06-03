x,y=[int(i) for i in input().split()]
if x > y:
    g = x
else:
    g = y

while(True):
    if((g % x == 0) and (g % y == 0)):
        lcm = g
        break
    g += 1
print(g)