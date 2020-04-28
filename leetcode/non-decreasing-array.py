# nums = [-1,-2,-3]
def checkPossibility(nums):
    i = 0
    j = 1
    count = 2
    while i < len(nums) -1 :
        print(nums[i],'--',nums[j])
        if nums[i] > nums[j]:
            count -= 1
            if count == 0:
                return (0)
            print(nums[j])

            continue

        i += 1
        j += 1
    if count == 0:
        return(0)
    else:
        return(1)
