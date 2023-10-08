import sys

input = sys.stdin.readline

n = int(input())
data = [input().split() for _ in range(n)]

sdata = sorted(data, key=lambda x: int(x[1]))
for name, score in sdata:
    print(name, end=' ')


"""
2
홍길동 95
이순신 77
"""