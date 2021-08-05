def remove_e(arr,n):
    for i in range(0,l):
        if li[i]!=n:
            res.append(li[i])
    return res

li=[1,1,2,3,4,4,5]
l=len(li)
res=[]
n=int(input("which element do you want to remove:"))
print(remove_e(res,n))
        
