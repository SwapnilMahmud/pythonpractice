k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
count=d
if(k==1 or l==1 or m==1 or n==1):
    print(count)
for i in range(d):
    if i%k!=0 and i%l!=0  and  i%m!=0  and  i%n!=0:
        count-=1

