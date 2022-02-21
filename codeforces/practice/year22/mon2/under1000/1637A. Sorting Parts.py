import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    if any([True if data[i - 1] > data[i] else False for i in range(1, n)]):
        print("YES")
    else:
        print("NO")