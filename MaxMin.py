# def Subarray(arr, k):
#     print(arr)
#     print('K:', k)
#     if len(arr) < k:
#         return 1
#     else:
#         print(sum(arr))
#         arr.pop()
#         return Subarray(arr, k)
#
#
# a = [1, 2, 3, 4, 5, 6]
#
# Subarray(a, 2)

def Subarray(arr, i, k):
    if i+1 >= len(arr) or len(arr[i:i+k]) != k:
        if len(arr) > k:
            arr = arr[1:]
            i = 0
            return Subarray(arr , i , k)
        else:
            return 1
    else:
        print(arr[i:i + k])
        return Subarray(arr, i + 1, k)


a = [1, 2, 3, 4, 5, 6]

Subarray(a, 0, 2)
