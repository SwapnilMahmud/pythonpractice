def BinarySearch(arr,data,n):
    l=0
    r=n-1
    while l<=r:
        m=(l+r)/2
        mid=int(m)
        if  data==arr[mid]:
            return mid
        elif data<arr[mid]:
            r=mid-1
        else:
            l=mid+1
    return -1
arr=[11,22,23,34,45,56,67,78,89,90]
data=89
n=len(arr)
print(BinarySearch(arr,data,n))
