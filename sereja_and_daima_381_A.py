n=int(input())
li=list(map(int,input().split()))
left=0
right=n-1
swapnil=0
saimu=0  
for i in range(right):
    if i%2==0 or i==0:
        if li[left]>li[right]:
            swapnil+=li[left]
            left+=1
        else:
            swapnil+=li[right]
            right=-1
    else:
        if li[left]>li[right]:
            saimu+=li[left]
            left+=1
        else:
            saimu+=li[right]
            right=-1
print(swapnil,saimu)
