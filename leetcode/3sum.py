nums = [-1, 1,0, 2, -1, -4 , 4, 5]
nums.sort()
numsdict = {}
i = 0
j = 1
while i < len(nums):
#     numsdict[nums[i]] = numsdict.get(nums[i],0)+1
    j = i + 1
    while j < len(nums):
        try:
            print(nums[i],nums[j],(nums[i]+nums[j])*-1)
            if numsdict[(nums[i]+nums[j])*-1]:
                print('Found')
#                 print(nums[i],nums[j],(nums[i]+nums[j])*-1)
        except KeyError as k:
            print('Err')
#             print('keyerror',k)
        j += 1
    i += 1
