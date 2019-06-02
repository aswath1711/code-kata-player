from collections import deque
# doube ended queue
#append() pop() rotate()
n,k = input().split()
k = int(k)
n = [x for x in input().split()]
d=deque(n)
d.rotate(k)
print(" ".join(d))
