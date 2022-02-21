n, m = map(int, input().split())
s = list(input().split())
t = list(input().split())

for _ in range(int(input())):
    y = int(input())
    print(s[(y + n - 1) % n] + t[(y + m - 1) % m])