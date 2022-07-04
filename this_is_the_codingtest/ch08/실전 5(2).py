import sys

n, m = map(int, input().split())
data = [int(input()) for i in range(n)]
memo = [sys.maxsize] * (m + 1)
memo[0] = 0 # 0에서 더해지는 것부터 생각하여 단위에 해당하는 인덱스 1로 채우는 과정 생략 가능

for i in range(3, m + 1):
    for j in range(n):
        if i - data[j] >= 0:
            memo[i] = min(memo[i], memo[i - data[j]] + 1)

print(memo[m] if memo[m] != sys.maxsize else -1)