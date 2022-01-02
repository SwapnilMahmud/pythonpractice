from collections import defaultdict
s=input()
t=input()
def minWindow(s,t):
    cnt=0
    dp=defaultdict(int)
    ds=defaultdict(int)
    for i in t:
        dp[i]+=1
    for i in s:
        ds[i]+=1
        print(i,"=",ds[i])
        if i in dp and ds[i]<=dp[i]:
            cnt+=1
            print("cnt=",cnt)
    print(dp)
    print(ds)
    print(cnt)
minWindow(s,t)
