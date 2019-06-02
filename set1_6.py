from collections import Counter
a,b=input().split()
a_counts = list(Counter(a).values())
b_counts = list(Counter(b).values())
if a_counts == b_counts:
    print("yes")
else:
    print("no")