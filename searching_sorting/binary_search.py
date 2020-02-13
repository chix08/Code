def binary_search(input_array, value):
    left = 0
    right = len(input_array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if input_array[mid] == value:
            return mid

        elif input_array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


a = [1, 3, 9, 11, 15, 19, 29]
value = 9
pos = binary_search(a, value)
print(pos + 1)
