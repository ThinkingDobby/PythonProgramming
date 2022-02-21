n = int(input())
data = list(map(int, input().split()))

cnt = -1
while n > 0:
    cnt += 1
    n -= data[cnt % 7]

print(cnt % 7 + 1)