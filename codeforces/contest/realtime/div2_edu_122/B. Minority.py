for _ in range(int(input())):
    data = input()
    one = data.count('1')
    zero = data.count('0')
    if one == zero:
        print(one - 1)
    else:
        print(min(one, zero))