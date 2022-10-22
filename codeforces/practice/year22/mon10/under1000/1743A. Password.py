import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = set([i for i in range(0, 10)]) - set(map(int, input().split()))

    print(math.comb(len(data), 2) * 6)