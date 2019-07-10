import numpy as np
arr = [1,3,4,5,6,7,8,9,10]

def mymedian(arr):
    return (sum(arr) / )

d = int(input())
t = d
notify = 0
for i in arr[d:]:
    print(arr[t-d:t])
    mn = np.median(arr[t-d:t])
    m = mymedian(arr[t-d:t])
    t += 1
    # print(i)
    print('nm',mn)
    print('m',m)
    if(i >= (2*m)):
        # print('m',2*m)
        notify += 1
print('notify',notify)