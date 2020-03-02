t = int(input())

while t:
    t -= 1
    n = int(input())
    largest = -2147483648
    for i in range(n):
        num = int(input())
        if num > largest:
            largest = num

    print (largest)