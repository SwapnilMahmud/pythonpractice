def ar():  
    bst=[ ]
    t=int(input("target:"))
    n=int(input("size:"))
    for i in range(0,n):
        e=int(input())
        bst.append(e)
        print("size:",bst)
    left=0
    right=len(bst)-1
    curr=bst[left]+bst[right]
    while left<=right:
        if curr<t:
            left+=1
        elif curr>t:
            right-=1
        else:
            return[left,right]
    return[-1,-1]    
ar()
