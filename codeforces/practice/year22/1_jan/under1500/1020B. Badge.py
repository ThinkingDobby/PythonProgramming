n = int(input())
data = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    memo = [0] * (n + 1)

    def func(x):
        memo[x] += 1
        if memo[x] == 2:
            print(x, end=' ')
            return
        func(data[x])

    func(i)