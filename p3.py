arr=[13,11,21,22,32,31,43,33]
data=31
found=0
n=len(arr)
for i in range(n):
    if data==arr[i]:
        print("data found position:",i)
        found=1
        break
if found==0:
    print("data not found")
        

