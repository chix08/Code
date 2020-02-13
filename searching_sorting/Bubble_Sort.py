def Bubblesort(temp_array):
    j = 1
    while j < len(temp_array):
        i = 0
        while i < len(temp_array) - j:
            print(temp_array[i])
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
            i += 1
        j += 1
    return a
a = [7,8,3,1,6]
ans = Bubblesort(a)
print(ans)