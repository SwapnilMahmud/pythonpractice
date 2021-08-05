sum all elements in array::::::
li=[1,2,3,3,4,5,5,6,7,7]
left=0
sum=0
right=len(li)-1
while left<=right:
    sum=sum+li[left]  
    left+=1
print(sum)
///////////////////////////////


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
::::::::::::::::::::::::::::::::::::////
import array
arr=array.array('i',[1,2,3,1,5])

print("the new array is :",end=" ")
for i in range(0,5):
    print(arr[i],end=" ")
print("\r")

print("poped element is :",end=" ")
print(arr.pop(0));

print("after pop array is :",end=" ")
for i in range(0,4):
    print(arr[i],end=" ")
print("\r")

arr.remove(5)
print ("The array after removing is : ",end="")
for i in range (0,3):
    print (arr[i],end=" ")
:::::::::::::::::::::::::::///////
import array
arr=array.array('i',[1,2,3,1,5])

print("the new array is :",end=" ")
for i in range(0,5):
    print(arr[i],end=" ")
print("\r")

print("poped element is :",end=" ")
print(arr.index(5));
arr.reverse()
print("after pop array is :",end=" ")
for i in range(0,5):
    print(arr[i],end=" ")
print("\r")



/////////////////////////////////

Rotation:::::::::::::::::::;
def firstfunction(arr,d,n):
    for i in range(d):
        secondfunction(arr,n)

def secondfunction(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp

def printA(arr,size):
    for i in range(size):
        print(arr[i], end=" ")
    
        
arr=[1,2,3,4,5,6,7]
firstfunction(arr,2,7)
printA(arr,7)
////////////////////////////////
li=[1,2,3,4,5,6,7]
n=len(li)
temp=0
temp=li[n-1]
for i in range(n-1,0,-1):
    li[i]=li[i-1]
li[0]=temp
print(li)

/////////////////////////////////////////////////
Remove duplicate element from array::::::::::::::::::::::::
li=[2,2,3,4,5,2,2,7,2,6,9,3,1]
l=len(li)-1
temp=0
count=0
s=int(input("enter number:"))
for i in range(l):
    if li[i]==s:
        temp=li[i]
    else:
        count+=1
        print("\n",li[i])
print("\ntotal number:",count)
    
//////////////////////////////////////////////////

def pairInSortedRotated( arr, n, x ):
    left=0
    right=n-1
    while left<right:
        curr=arr[left]+arr[right]
        if curr<x:
            left+=1
        elif curr>x:
             right-=1
        else:
             return True
    return False
  
arr = [ 6, 8, 9, 10,11, 15,]
sum = 32
n = len(arr)
if (pairInSortedRotated(arr, n, sum)):
	print ("Array has two elements with sum")
else:
	print ("Array doesn't have two elements with sum  ")

	

///////////////////////////////////////////////
n=int(input("please give an array size:"))
arr=[0]*n
for i in range(0,n):
    e=int(input())
    arr[i]=e
print("Total arrays are:")
for i in range(0,n):
    print("",arr[i])
..........................................
max:::::::::::::::::::::
li=[1,2,3,4,59,5,7,198,543,555,76,542]
l=len(li)
max=0
for i in range(l):
    if max<li[i]:
        max=li[i]
print(max)
min::::::::::::::::::::
li=[-1,2,3,4,59,5,0,7,198,543,555,76,542]
l=len(li)
min=li[0]
for i in range(l):
    if min>li[i]:
        min=li[i]
print(min)

::::::::::::::take input from user::
m=list(map(int,input().split()))
.......................
.......................
reverse:

li=[1,2,3,4,5]
for i in range(len(li)-1,-1,-1):
    print(li[i])
::::::::::::::::::::::
print array
li=[1,2,3,4,5]
for i in range(len(li)):
    print(li[i])
::::::::::::::::::
enter element in an giving position:
li=[1,2,3,4,5,]
n=int(input("Enter an element:"))
p=int(input("Enter the position:"))
li.append(-1000)
print("size list:",li)
print("working on while loop:")
for i in range(4, p-2,-1):
    li[i+1]=li[i]
    print(li)
li[p-1]=n
print("Finish list:",li) 

:::::::::::::
searching number if found return index or not then return -1
li=[1,2,3,4,5,6,7]
s=int(input("searching number:"))
l=len(li)
e=0
if s not in li:
    print("-1")
else:
    print( li.index(s))