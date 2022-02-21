import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [[input().rstrip(), i + 1] for i in range(n)]
ans = sorted(data, key=lambda x: [ord(x[0][i]) * (-1 if i % 2 == 1 else 1) for i in range(m)])
print(*[i[1] for i in ans])