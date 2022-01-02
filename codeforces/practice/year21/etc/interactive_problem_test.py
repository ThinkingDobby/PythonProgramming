# 1. Guess the Number

import sys

l = 1
r = 1_000_000

while l < r:
    mid = (l + r + 1) // 2
    print(mid)
    # sys.stdout.flush()    # 버퍼 사용 x - 안 붙여도 됨
    data = input()
    if data == '>=':
        l = mid
    else:
        r = mid - 1
print('!', r)
