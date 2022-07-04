array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

memo = [0] * (max(array) + 1)

for i in array:
    memo[i] += 1

for i in range(len(memo)):
    for _ in range(memo[i]):
        print(i, end=' ')