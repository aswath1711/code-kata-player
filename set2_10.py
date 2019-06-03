n=input()
lis=list(n)
for i in range(len(lis)):
    asc=ord(lis[i])
    if(asc==88):
        lis[i]="A"
    elif(asc==89):
        lis[i]="B"
    elif(asc==90):
        lis[i]="C"
    else:  
        lis[i]=chr(asc+3)
print("".join(lis))
    
