def merge(array, left, m , right):
    sarray = array.copy()
    print(array[left:m])
    print(array[m:right])
    i = left
    j = m
    sp = 0
    while i < m and j < right:
        if a[i] > a[j]:
            sarray[sp] = a[j]
            j += 1
        else:
            sarray[sp] = a[i]
            i += 1
        sp += 1

    pass




def mergesort(a, l , r):
    if l < r:
        m = (l + r)//2
        mergesort(a, l , m)
        print()
        mergesort(a, m+1, l)
a = [12, 11, 13, 5, 6, 7, 18]

mergesort(a,0,len(a))