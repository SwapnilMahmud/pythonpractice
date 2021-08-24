n=int(input())
cnt=0
for i in range(n):
    li=list(map(int,input().split()))
    cnt_1=0
    for j in li:
        if j==1:
            cnt_1+=1
    print(cnt_1)
    if cnt_1>=2:
        cnt+=1
print(cnt)
