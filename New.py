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
li.pop()
li.pop()
print(li)
print(len(li))
print(li[2])
print(li[3])
print("..............................................for searching")

for element in li:
    print(element)
print("..............................................")



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

target=8
for element in li:
    if target==element:
        print("found")
    else:
        print("not found")
        
		
		
start=len(li)-1
while start>=0:
    print(li[start])
    start-=1
    




    
