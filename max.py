li=[-1,2,3,4,59,5,0,7,198,543,555,76,542]
l=len(li)
min=li[0]
for i in range(l):
    if min>li[i]:
        min=li[i]
print(min)
