import math

for _ in range(int(input())):
    n = int(input())
    tmp = 2**int(math.log(n - 1, 2))
    for i in range(tmp - 1, -1, -1):
        print(i, end=' ')
    for i in range(tmp, n):
        print(i, end=' ')
    print()
