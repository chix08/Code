def mergesort(array):
    left = 0
    right = len(array)
    mid = (left + right)//2
    L = array[:mid]
    R = array[mid:]
    if mid > 0:
        mergesort(L)
        mergesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i+=1
            else:
                array[k] = R[j]
                j+=1
            print(array)
            k+=1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1








arr = [16, 11, 13,1,3,9, 5, 6, 7]
mergesort(arr)
print()