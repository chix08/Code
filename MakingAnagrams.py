from collections import Counter

# def makeAnagram(a, b):
#     count = 0
#     dict1 = Counter(a)
#     dict2 = Counter(b)
#     c = dict1 & dict2
#     for i in c:
#         count += c[i]
#     ans = len(a) + len(b) - count - count
#     return ans
a = 'fcrxzwscanmligyxyvym'
b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
res = number_needed(a,b)
print(res)