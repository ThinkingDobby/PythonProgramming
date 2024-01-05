import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    tmp = int(math.sqrt(sum(data)))
    print("YES" if tmp * tmp == sum(data) else "NO")