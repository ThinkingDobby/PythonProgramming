h, m = input().split(':')
t = int(h) * 60 + int(m)

if t in range(5 * 60 + 51, 10 * 60 + 1 + 1):
    print(10 * 60 + 1 - t)
elif t in range(15*60 + 52, 20 * 60 + 2 + 1):
    print(20 * 60 + 2 - t)
elif t in range(23 * 60 + 33, 24 * 60):
    print(60 - int(m))
elif int(h[::-1]) < int(m):
    print(int(h[::-1]) + 10 + 60 - int(m))
else:
    print(int(h[::-1]) - int(m))