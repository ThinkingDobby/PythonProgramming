a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())


tmp = min(a, d)
dt = d - tmp
fc = e * tmp + f * min(c, b, dt)

tmp = min(c, b, d)
d -= tmp
sc = f * tmp + e * min(a, d)

print(max(fc, sc))
