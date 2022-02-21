n = int(input())

memo = {}
for i in range(n):
    data = input().split()
    memo[data[0]] = 100 * int(data[1]) - 50 * int(data[2]) + sum(map(int, data[3:]))

print(sorted(memo.keys(), key=lambda x:memo[x])[-1])