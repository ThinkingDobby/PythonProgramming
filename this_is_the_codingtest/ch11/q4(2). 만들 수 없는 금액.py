n = int(input())
data = sorted(map(int, input().split()))

target = 1
for i in data:
    if i > target:
        break
    target += i

print(target)