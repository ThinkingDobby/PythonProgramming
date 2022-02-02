n, m = map(int, input().split())

a = list(range(1, min(n * 2, m) + 1))
b = list(range(n * 2 + 1, m + 1))
while a or b:
    if b:
        print(b.pop(0), end=' ')
    if a:
        print(a.pop(0), end=' ')