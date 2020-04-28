nums = [0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]
d = {1:0,0:0}
for i in nums:
    d[i] = d.get(i,0)+1
if d[0]>d[1]:
    more = 0
elif d[1]>d[0]:
    more = 1
else:
    print(d[0]+d[1])
i = 0
j = len(nums)-1
print(more,i,j,d)
while d[0]!=d[1] and j > i:
    print('nums[i] -->', nums[i])
    if nums[i] == more:
        d[nums[i]] -= 1
        i += 1
    else:
        d[nums[j]] -= 1
        j -= 1
        
    print(i,j,d)
if d[0]== d[1]:
    print(d[0]+d[1])
else:
    print(0)
    
    
    
    
    
