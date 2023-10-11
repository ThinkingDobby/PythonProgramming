import math

cnt = 0
for i in range(1, 11):
    cnt += math.comb(10, i) * 2**i

print(cnt)