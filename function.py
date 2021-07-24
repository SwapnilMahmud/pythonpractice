def two_sum(bst,t):
    left=0
    right=len(bst)-1    
    while left<=right:
            curr=bst[left]+bst[right]
            if curr<t:
                left+=1
            elif curr>t:
                right-=1
            else:
                return[left,right]
     return[-1,-1]
bst=[ 1,9,4,3,5,7]
t=9
print(two_sum(bst,t))
  
