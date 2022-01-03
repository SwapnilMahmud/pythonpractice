li=[]
li.append(3)
li.append(4)
li.append(5)
li.append(6)
li.append(7)
li.append(8)
li.append(9)
li.append(10)
li.append(11)
print(li)
s=0
e=len(li)-1
while s<e:
    temp=li[s]
    li[s]=li[e]
    li[e]=temp
    s+=1
    e-=1
print(li)
    




    
