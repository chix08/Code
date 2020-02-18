def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)


def partition(array, low, high):
    left = low
    pivot = array[high]
    right = high - 1
    while left <= right and pivot > 0:
        if array[left] > pivot:
            array[left], array[right] = array[right], array[left]
            right -= 1
        else:
            left += 1
    array[left], array[high] = array[high], array[left]
    return left

array = [15,1,8,4,3,9,7,50,12,11]

low = 0
high = len(array) - 1
na = quick_sort(array, low, high)
print(array)