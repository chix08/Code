nums = [2, 7, 11, 15]
target = 9
i = 0
d = {}
while i < len(nums):
    print(i)
    if d.get(target - nums[i]):
#         print(d.get(target - nums[i]))
        return(d.get(target - nums[i])[1],i)
    d[nums[i]] = [nums[i],i]
    i += 1
