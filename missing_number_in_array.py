li=[10,11,12,13,14,16,17,18,19,20]
n=len(li)
s=0
while s<n:
    for i in range(10,20):
        if li[s] != i:
            print("missing:",li[i])
            s+=1
