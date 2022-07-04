n, m = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0
for i in range(n - 1):
    for j in range(i, n):
        if data[i] != data[j]:
            cnt += 1

print(cnt)

"""
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
"""