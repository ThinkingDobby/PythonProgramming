import math

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    memo = [0] * 12

    for i in data:
        if i <= 2048:
            memo[int(math.log(i, 2))] += 1

    for i in range(1, 12):
        memo[i] += memo[i - 1] // 2

    if memo[11] >= 1:
        print("YES")
    else:
        print("NO")