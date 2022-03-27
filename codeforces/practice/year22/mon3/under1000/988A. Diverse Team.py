import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))
if len(set(data)) >= k:
    print("YES")
    for i in set(data):
        print(data.index(i) + 1, end=' ')
        k -= 1
        if k == 0:
            break
else:
    print("NO")