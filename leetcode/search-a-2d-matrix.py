# Python Program for recursive binary search. 

# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
    if r >= l: 

        mid = l + (r - l)//2

        if arr[mid] == x: 
            return mid 

        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 

        else: 
            return binarySearch(arr, mid+1, r, x) 

    else:
        return [l,r]

# Test array 
arr = [23,30,34,50]
x = 51
result = binarySearch(arr, 0, len(arr)-1, x) 
