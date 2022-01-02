k=0
max=0
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    k=b-a+k
    if (max<k):
        max=k
print(max)

