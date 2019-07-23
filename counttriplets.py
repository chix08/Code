# Complete the countTriplets function below.
def countTriplets(arr, r):
    count = 0
    tripletcount = {}
    # temptriplet = []

    for index, value in enumerate(arr):
        tripletcount[value] = tripletcount.get(value, [])
        tripletcount[value].append(index)
    sarr = set(arr)
    for value in sarr:
        try:
            first = tripletcount[value]
            second = tripletcount[value * r]
            third = tripletcount[value * r * r]

            for i in first:
                for j in second:
                    for k in third:
                        if (i < j < k):
                            print(i, j, k)
                            count += 1

        except Exception as e:
            continue
    print('count', count)


r = 3

arr = [1, 3, 9, 9, 27, 81]

ans = countTriplets(arr, r)
