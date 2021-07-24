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


