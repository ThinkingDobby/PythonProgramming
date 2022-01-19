n, k = map(int, input().split())
data = list(map(int, input().split()))
memo = [0] * k
for i in range(n):
    memo[i % k] += data[i]

s = sum(data)
print(max(map(lambda x: abs(s - x), memo)))
