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

swapping in kth element::::::::::::::::::::::::::::
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


/////////////////

took array element from user:::::::::::::::::::::
n=int(input("please enter the array size n:"))
li=[0]*n
print(li)
for i in range(0,n):
    e=int(input())
    li[i]=e
    print(li)   

///////////////////////

a number how many times in an array:::::::: 
k=int(input("what number do you want to check k:"))
n=int(input("Enter the size of array n:"))
count=0
li=[0]*n
left=0
right=len(li)
for i in range(0,n):
    e=int(input())
    li[i]=e
print("all arrays are:",li)
for el in range(0,right):
    if li[el]==k:
        count+=1
print("total numbers:",count)

////////////////////////////////

intersection:::::::::::::::::::::::
li1=[1,3,4,5,6]
li2=[2,3,4,9,8,6,1]
x=len(li1)
y=len(li2)
for l in range(0,x):
    for m in range(0,y):
        if li1[l]==li2[m]:
            print(li1[l])
            
//////////////////////////////

print array:::::::::::::::::::::::
import array as arr
array_num=arr.array('i',[10,11,12,13,14,15,16,17,18,19,20])
print("arrays:")
for i in range(len(array_num)):
    print(array_num[i], end=' ')

////////////////////////////////////

misssing number in an array::::::::::::


import array as arr
def two_sum(nums):
    return sum(range(10,21))-sum(list(nums))

array_num=arr.array("i",[10,11,12,13,14,15,16,18,19,20])
print("orginal array:")
for i in range(len(array_num)):
    print(array_num[i],end=" ")
print("\nmissing number in array:",two_sum(array_num))
        
-
    ////////////////////////////////////////
    
    remove duplicate array:::::::::::::
    
    li=[1,2,2,3,4,4,5,7,7,7,7,7]
res=[]
for i in li:
    if i not in res:
        res.append(i)
print(res)

/////////////////////////////////////

def remove_e(arr,n):
    for i in range(0,l):
        if li[i]!=n:
            res.append(li[i])
    return res

li=[1,1,2,3,4,4,5]
l=len(li)
res=[]
n=int(input("which element do you want to remove:"))
print(remove_e(res,n))
    
//////////////////////////////

array:

import array


arr=array.array('i',[1,2,3])
print("new array is :",end=" ")
for i in range(0,3):
    print(arr[i],end=" ")
print("\r")

arr.append(4)
print("append array is :",end=" ")
for i in range(0,4):
    print(arr[i],end=" ")
print("\r")

arr.insert(2,6)
print("after insertion array is :",end=" ")
for i in range(0,5):
    print(arr[i],end=" ")

