def get_fib(position):
    # if position == 0 or position == 1:
    #     return position
    # return get_fib(position - 1) + get_fib(position - 2)
    if position == 0 or position == 1:
        return 1
    else:
        output = get_fib(position-1) + get_fib(position-2)
        return output





