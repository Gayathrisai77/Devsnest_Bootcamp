nums = [6,2,-3,4,2,1,8,-2]
globalsum = nums[0]
currsum = 0
for n in nums:
    currsum = currsum+n
    if currsum < 0:
        currsum = 0
    else:
        globalsum = max(globalsum,currsum)
print(globalsum)