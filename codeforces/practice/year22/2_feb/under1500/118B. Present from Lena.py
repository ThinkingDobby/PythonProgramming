n = int(input())

for i in range(0, n + 1):
    print((n - i) * 2 * ' ', end='')
    for j in range(0, i + 1):
        print(j, end='' if j == 0 and j == i else ' ')
    for j in range(i - 1, -1, -1):
        print(j, end='' if j == 0 else ' ')
    print()

for i in range(n - 1, -1, -1):
    print((n - i) * 2 * ' ', end='')
    for j in range(0, i + 1):
        print(j, end='' if j == 0 and j == i else ' ')
    for j in range(i - 1, -1, -1):
        print(j, end='' if j == 0 else ' ')
    print()
