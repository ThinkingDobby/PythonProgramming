data = input()

lev = 0
for i in range(len(data)):
    if i < len(data) - 1:
        if data[i + 1] == '<':
            print(data[i])
            if data[i + 2] == '/':
                lev -= 1
            if data[i - 2] != '/':
                lev += 1
            print(' ' * 2 * lev, end='')
        else:
            print(data[i], end='')
    else:
        print(data[i], end='')
