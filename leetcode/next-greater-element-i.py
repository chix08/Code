nums1 = [4,1,2]
nums2 = [1,3,4,2]
checkdi = {}
checlist = [-1] * len(nums2)
stack = []

for i in range(len(nums2)-1,-1,-1):
    while stack:
        if nums2[i] < stack[-1][0]:
            checlist[i] = stack[-1][0]
            break
        else:
            stack.pop()
    checkdi[nums2[i]] = i
    stack.append([nums2[i],i])
ans = []
for j in nums1:
    ans.append(checlist[checkdi[j]])

print(ans)