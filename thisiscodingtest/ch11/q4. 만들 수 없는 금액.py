n = int(input())
data = sorted(map(int, input().split()))

target = 1
for i in data:
    if i > target:
        break
    target += i

print(target)

"""
5
3 2 1 1 9
"""