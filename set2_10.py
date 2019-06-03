n=input()
lis=list(n)
for i in range(len(lis)):
    lis[i]=chr(ord(lis[i])+3)
print("".join(lis))
    