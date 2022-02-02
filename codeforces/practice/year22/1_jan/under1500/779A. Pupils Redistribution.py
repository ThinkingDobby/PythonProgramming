n = int(input())
memo = [0] * 6
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in a:
    memo[i] += 1
for i in b:
    memo[i] -= 1

if all([memo[i] % 2 == 0 for i in range(5)]):
    print(sum([i for i in memo if i > 0]) // 2)
else:
    print(-1)