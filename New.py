nums=[3,2,2,3]
i=0
r=0
val=3
while i<len(nums):
    if nums[i]!=val:
        nums[r]=nums[i]
        r+=1
    i+=1
print(nums)
