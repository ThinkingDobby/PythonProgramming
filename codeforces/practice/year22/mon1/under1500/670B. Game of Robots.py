n, k = map(int, input().split())
data = list(map(int, input().split()))

i = 1
while True:
    if i * (i + 1) // 2 >= k:
        break
    i += 1

print(data[k - i * (i - 1) // 2 - 1])