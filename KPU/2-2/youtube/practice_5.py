# 1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) # 10에서 7을 뺀 3을 출력

# 2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100: self.value = 100

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print(cal.value) # 100 출력

# 3
# false, true

# 4
print(list(filter(lambda a: a >= 0, [1, -2, 3, -5, 8, -3])))

# 5
print(int('0xea', 16))

# 6
result = list(map(lambda a: a * 3, [1, 2, 3, 4]))
print(result)

# 7
input = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(input) + min(input))

# 8
print(round(17 / 3, 4))

# 9
# import sys
# print(sum(sys.args))

# 10
# 11

# 12
import time
print(time.strftime("%Y/%m/%d %H:%M:%S"))

# 13
import random
result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num in result: continue
    else: result.append(num)
print(result)