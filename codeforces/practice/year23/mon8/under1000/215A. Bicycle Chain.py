import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

mv = -1
cnt = 0
for i in range(n):
    for j in range(m):
        if b[j] % a[i] == 0:
            if b[j] // a[i] > mv:
                mv = b[j] // a[i]
                cnt = 1
            elif mv == b[j] // a[i]:
                cnt += 1

print(cnt)
