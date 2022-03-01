n = int(input())
data = list(input())
i = 0

while i < n:
    if i < n - 1:
        if data[i:i + 2] == ['B', 'B']:
            print('A', end='')
            i += 2
            continue
        elif data[i:i + 2] == ['B', 'A']:
            data[i] = 'A'
            data[i + 1] = 'B'
            print('A', end='')
            i += 1
            continue

    print(data[i], end='')
    i += 1
