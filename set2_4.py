s=input()
stri=list(s)
for ch in stri:
    if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        stri.remove(ch)      
print("".join(stri))