import decimal
import math
import sys
inp = sys.stdin.readline

for _ in range(int(inp())):
    x, y, k = map(int, inp().split())
    print(math.ceil((decimal.Decimal(k + y * k) - 1) / (x - 1)) + k)    # 연산 전에 decimal.Decimal로 연산자 감싸주면 부동소수점 오차로부터 자유로움


# 참조한 코드 - ceil을 사용하지 않으면 부동소수점 오차 발생하지 않음
for _ in range(int(input())):
    x, y, k = [int(s) for s in input().split()]
    n = ((y + 1) * k - 1 + (x - 2)) // (x - 1)
    print(n + k)