import math

n = int(input())
data = [int(input()) for _ in range(int(n))]

cnt = 0
for i in range(n):
    if data[i] % 2 == 1:
        if cnt:
            print(math.floor(data[i] / 2))
        else:
            print(math.ceil(data[i] / 2))
        cnt ^= 1
    else:
        print(data[i] // 2)