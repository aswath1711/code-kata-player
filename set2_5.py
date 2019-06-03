s=input()
n=list(s)
max_count=0
val=""
for i in range(len(n)):
    if n.count(n[i])>max_count:    
        max_count= n.count(n[i])
        val=n[i]
print(val)
