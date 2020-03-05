string = ['a', 'b', 'x', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'y']
pattern = ['c', 'a']
j = 0
i = 1
pre_suf_l = [-1 for _ in range(len(pattern))]
pre_suf_l[0] = 0
while i < len(pattern):
    if pattern[j] != pattern[i] and j == 0:
        pre_suf_l[i] = 0
        i += 1
    elif pattern[j] != pattern[i] and j != 0:
        j = pre_suf_l[j - 1]
    else:
        pre_suf_l[i] = (j + 1)
        j += 1
        i += 1
count = 0
i = 0
j = 0
while i < len(string):
    if j < len(pattern) and string[i] == pattern[j]:
        i += 1
        j += 1
    else:
        if 0 < j < len(pattern):
            j = pre_suf_l[j - 1]
        if j >= 0 and string[i] != pattern[j]:
            i += 1
    if j >= len(pattern):
        count += 1
        j = 0
print('COUNT', count)
