l = []

for _ in range(int(input())):
    iv = input().split()
    l.append(iv)

s_iv = sorted(l, key = lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(s_iv[-1][0])
print(s_iv[0][0])