x, y, z = map(int, input().split())

a = x if x % z < y % z else y
b = y if x % z < y % z else x

tmp = a % z

if (b + tmp) // z > b // z:
    rest = (b + tmp) % z
    print((a - tmp) // z + (b + tmp) // z, tmp - rest)
else:
    print(a // z + b // z, 0)