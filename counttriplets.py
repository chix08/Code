# Complete the countTriplets function below.
def countTriplets(arr, r):
    count = 0
    tripletcount = {}
    temptriplet = []


    for index, value in enumerate(arr):
        tripletcount[value] =  tripletcount.get(value , [])
        tripletcount[value].append(index)
    sarr = set(arr)
    for value in sarr:
        temptriplet.append([value , value * r, value*r*r])

    for i in temptriplet:
        try:
            first = tripletcount[i[0]]
            second = tripletcount[i[1]]
            third = tripletcount[i[2]]

            for i in first:
                for j in second:
                    for k in third:
                        if(i<j<k):
                            print(i, j, k)
                            count += 1

        except Exception as e:
            print(e)
            continue
    print('count',count)

