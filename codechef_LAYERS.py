t = int(input())

while t:
    a = []
    n, colors = (map(int, input().split()))
    t -= 1
    for i in range(n):
        a.append(list((map(int, input().split()))))
    x_ax = {new_list: 0 for new_list in range(1, colors + 1)}
    y_ax = {new_list: 0 for new_list in range(1, colors + 1)}
    sum_x = 0
    sum_y = 0
    rslt = ['0'] * (colors + 1)
    while a:
        temp = a.pop()
        x = temp[0] // 2
        y = temp[1] // 2
        c = temp[2]
        if x > sum_x:
            diff = x - sum_x
            x_ax[c] += diff
            sum_x += diff
            y_ax[c] += y
        if y > sum_y:
            diff = y - sum_y
            y_ax[c] += diff
            sum_y += diff
            x_ax[c] += x

    print()
    print(x_ax)
    print(y_ax)
    for i, j in zip(x_ax, y_ax):
        if x_ax[i] and y_ax[j]:
            r = x_ax[i] * y_ax[j] * 4
            rslt[i] = str(r)
        # if x_ax[i] != 0 and y_ax[j] == 0:
        #     r = x_ax[i] * x_ax[i] * 4
        #     rslt[i] = str(r)
        # if y_ax[j] != 0 and x_ax[i] == 0:
        #     r = y_ax[j] * y_ax[j] * 4
        #     rslt[j] = str(r)

    rs = ' '.join(rslt[1:])
    print(rs)
