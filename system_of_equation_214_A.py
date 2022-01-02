import math
n,m=map(int,input().split())
cnt=0
a=int(math.sqrt(n))+2
b=int(math.sqrt(m))+2
for i in range(a):
    for j in range(b):
        if i**2+j==n and j**2+i==m:
            cnt+=1
print(cnt)

