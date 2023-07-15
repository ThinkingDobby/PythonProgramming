mod = 998244353
n = int(input())
l = len(str(n))

tmp = 0
for i in range(1, l):
    a = 9 * 10 ** (i - 1)
    tmp = (tmp + a * (a + 1) // 2) % mod

a = n - 10**(l - 1) + 1
tmp = (tmp + a * (a + 1) // 2) % mod

print(tmp)