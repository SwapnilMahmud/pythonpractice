def BinarySearch(arr,n,data):
    l=0
    r=n-1
    while l<=r:
        m=(l+r)/2
        mid=int(m)
        if data==arr[mid]:
            return mid
        elif data<arr[mid]:
            r=mid-1
        else:
            l=mid+1
    return -1

arr=[10,22,34,55,57,67,70,88,99]
data=99
l=len(arr)
print(BinarySearch(arr,l,data))
