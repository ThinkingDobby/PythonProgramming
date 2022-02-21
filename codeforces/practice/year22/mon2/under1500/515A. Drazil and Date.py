a, b, s = map(int, input().split())
dist = abs(a) + abs(b)
if s < dist:
    print("No")
else:
    if (s - dist) % 2 == 0:
        print("Yes")
    else:
        print("No")