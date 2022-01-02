n=int(input())
li=list(map(int,input().split()))
p=[0]*n
for i in range(n):
    p[li[i]-1]=i+1
for i in range(n):
    print(p[i],end=" ")
    
