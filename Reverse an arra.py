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
    

   
   
