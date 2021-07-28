li=[1,66,2,61,3,4,10,66]
li.sort()
q=len(li)
temp=0
for e in range(0,q):
    for f in range(1,q):
        if li[e]==li[f]:
            li.pop(e)
print(li)
