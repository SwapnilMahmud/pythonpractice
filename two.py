def two_sum(bst,t):
    left=0
    right=len(bst)-1
    while left<right:
        curr=bst[left]+bst[right]
        if curr<t:
            left+=1
        elif curr>t:
            right-=1
        else:
            return[left,right]
    return[-1,-1]
bst=[]
t=int(input("target:"))
n=int(input("size:"))
for i in range(0,n):
        e=int(input())
        bst.append(e)
        bst.sort()
print(two_sum(bst,t))
  

