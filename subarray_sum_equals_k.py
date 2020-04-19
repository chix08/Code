
#For positive Integer
left = 0
right = 0
nums = [-1,-1,1]
# nums = [1, 4, 7, 10, 2, 12, 14,11,1,2,9]
n = len(nums)
k = 0
# count = 0
# sumnow = 0
# while left < n and right < n and left <= right:
#     if k > sumnow:
#         sumnow += nums[right]
#         right += 1
#     else:
#         sumnow -= nums[left]
#         left += 1
#     if sumnow == k:
#         count += 1
#         # print(nums[left:right])
# while left <n and left != right:
#     sumnow -= nums[left]
#     left += 1
#     if sumnow == k:
#         count += 1


# print(count)

# For any integer
count = 0
d = {0:1}
sum = 0
for i in nums:
    sum += i
    if d.get(sum-k):
        count += d.get(sum-k)
    d[sum] = d.get(sum,0)+1
print(count)