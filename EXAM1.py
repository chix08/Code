test = int(input())
for _ in range(test):
    num = int(input())
    num -= 1
    i = 0
    count = 0
    right_str = input()
    answer_str = input()
    while i < num:
        if (answer_str[i] == 'N'):
            i += 1
            continue
        if (right_str[i] == answer_str[i]):
            i += 1
            count += 1
        else:
            i += 2

    if answer_str[-1] == right_str[-1] and right_str[-1] != 'N':
        count += 1
        print(count)
    else:
        print(count)
    # DDCABCCCA
    # DNCBBBBBA
