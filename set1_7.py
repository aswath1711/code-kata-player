y=input()
x=list(y)
for i in range(0,len(x),2):
    j=i+1
    x[i],x[j]=x[j],x[i]
print("".join(x))
    