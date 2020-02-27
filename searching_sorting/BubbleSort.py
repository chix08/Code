def bubblesort(arr):
    swap = 0
    j = len(arr) - 1
    while j:
        j -= 1
        for i in range(len(arr)-1):
            if(arr[i] >= arr[i+1]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swap += 1
    return swap

arr = [3, 9, 5, 71, 1]
a = bubblesort(arr)
print(a)
'''
[3, 9, 5, 71, 1]
[3, 5, 9, 1, 71]
[3, 5, 1, 9, 71]
[3, 1, 5, 9, 71]
[1, 3, 5, 9, 71]
'''