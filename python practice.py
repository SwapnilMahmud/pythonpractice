li1=[1,3,4,5,6]
li2=[2,3,4,9,8,6,1]
x=len(li1)
y=len(li2)
for l in range(0,x):
    for m in range(0,y):
        if li1[l]==li2[m]:
            print(li1[l])
            
