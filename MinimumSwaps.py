def minimumswaps(arr, n):
    count = 0
    array_dict = {}
    check = [False for _ in range(n + 1)]
    for i, j in enumerate(arr):
        array_dict[j] = i + 1
    for key, value in sorted(array_dict.items(), key=lambda x: x[0]):
        if check[key] or key == value:
            continue
        t_count = 0
        value = key
        while not check[value]:
            check[value] = True
            value = array_dict[value]
            t_count += 1
        count += t_count - 1
    return count
