n = int(input())
data = list(map(int, input().split()))

i = 1
while i < n and data[i - 1] < data[i]:
    i += 1
while i < n and data[i - 1] == data[i]:
    i += 1
while i < n and data[i - 1] > data[i]:
    i += 1

print("YES" if i == n else "NO")