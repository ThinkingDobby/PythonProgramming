n = int(input())
memo = "aabb"
for i in range(n):
    print(memo[i % 4], end='')