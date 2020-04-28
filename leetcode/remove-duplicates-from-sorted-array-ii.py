nums = [0,0,1,1,1,1,2,3,3]
count = 0
i = 0
while i < (len(nums) - 1):
    if nums[i] == nums[i+1]:
        count += 1
#         print('c',count)
        if count > 1:
            del(nums[i+1])
            continue
    try:
        if nums[i] != nums[i+1]:
#             print('TRY')
            count = 0
    except:
        continue
    i += 1
print(nums)
