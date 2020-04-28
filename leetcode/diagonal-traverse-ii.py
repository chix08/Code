
# nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
j = 0
ans = []
while len(nums):
    i = j
    while i >= 0: 
        if len(nums[i]) > 0:
            ans.append(nums[i].pop(0))
        else:
            del (nums[i])
            print('n',nums,i)
            j -= 1
        i -= 1
    j += 1
    if j >= len(nums):
        j = len(nums) - 1

        
        
