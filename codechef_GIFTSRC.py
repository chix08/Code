



t = int(input())

while t:
    check = {'L': ['L', 'R'], 'R': ['L', 'R'], 'U': ['D', 'U'], 'D': ['D', 'U'], 'P': []}
    prev_seq = 'P'
    x, y = 0, 0
    num = int(input())
    seq = list(input())
    t -= 1
    for i in seq:
        if i not in check[prev_seq]:
            prev_seq = i
            if i == 'L':
                x -= 1
                continue
            if i == 'R':
                x += 1
                continue
            if i == 'U':
                y += 1
                continue
            if i == 'D':
                y -= 1
                continue
    print(x,' ',y)
