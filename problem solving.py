sum all elements in array::::::
li=[1,2,3,3,4,5,5,6,7,7]
left=0
sum=0
right=len(li)-1
while left<=right:
    sum=sum+li[left]  
    left+=1
print(sum)
//////////////////////////////


Reverse an array:::::::::::::::
li=[1,2,3,4,5]
left=0
right=len(li)-1
while left<=right:
   print(li[right])
   right-=1
//////////////////////


multiplication of two:
li=[1,2,3,4,5,6,7,8,9,10]
r=len(li)
l=0
for e in range(0,r):
    l=2*li[e]
    print(l)
/////////////////////


find even number in an array::::::
li=[1,2,3,4,5,6,7,8,9,10]
r=len(li)
l=0
for e in range(0,r):
    if li[e]%2==0:
        print(li[e])
///////////////////////


count total even no in an array:::::
li=[1,2,3,4,5,6,7,8]
r=len(li)
count=0
for e in range(0,r):
    if li[e]%2==0:
        count+=1
print(count)
///////////////////////////////


in an array all even number addition::::::
li=[1,2,3,4,5,6,7,8,10]
r=len(li)
sum=0
count=0
for e in range(0,r):
    if li[e]%2==0:
        sum=sum+li[e]
print(sum)
/////////////////////////////

find the large number in an array::::::
li=[1,66,2,61,3,4,10,51]
li.sort()
q=len(li)
temp=0
for e in range(0,q):
    for f in range(1,q):
        if li[e]<li[f]:
            temp=li[f]
print(temp)
////////////////////////////////////

swap by python:::::::::::::::::::::
a=20
b=10
temp=0
print("before swap a:",a)
print("before swap b:",b)
temp=a
a=b
b=temp
print("after swap a:",a)
print("after swap b:",b)

///////////////////////////////////

k=int(input("please enter the swap element:"))
n=int(input("please enter the array size:"))
temp=0
li=[0]*n
print("before taking input:",li)
for i in range(0,n):
    e=int(input())
    li[i]=e
print(li)
print("before swapping arrays are:",li)
temp=li[k-1]
li[k-1]=li[n-k]
li[n-k]=temp
print("after swapping arrays are:",li)
    