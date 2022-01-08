memo = [int(str(i) * j) for j in range(1, 10) for i in range(1, 10)]

for _ in range(int(input())):
    n = int(input())

    s = 0
    for i in range(len(memo)):
        if memo[i] > n:
            break
        s += 1

    print(s)