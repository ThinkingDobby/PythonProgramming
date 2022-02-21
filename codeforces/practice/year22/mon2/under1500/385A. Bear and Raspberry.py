n, c = map(int, input().split())
data = list(map(int, input().split()))

mv = 0
for i in range(1, n):
    mv = max(mv, data[i - 1] - (data[i] + c))

print(mv)