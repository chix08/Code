test = int(input())
while test:
    test -= 1
    i = int(input())
    a = (i % 12) * 2
    if (a != 0):
        seat = 13 - a
    else:
        seat = -11
    seat = i + seat

    check = {0: 'WS', 1: 'WS', 2: 'MS', 5: 'MS', 3: 'AS', 4: 'AS'}

    print(seat, check[seat % 6])