st,en=[int(x) for x in input().split()]
count=0
for val in range(st, en + 1): 
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           count+=1 
print(count)