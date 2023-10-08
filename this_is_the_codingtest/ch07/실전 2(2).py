import sys

input = sys.stdin.readline


def binary_search(data, target, l, r):
    while l <= r:
        mid = (l + r) // 2

        if data[mid] < target:
            l = mid + 1
        elif data[mid] > target:
            r = mid - 1
        else:
            return mid


n = int(input())
data = sorted(map(int, input().split()))
m = int(input())
order = list(map(int, input().split()))

for i in order:
    print("yes" if binary_search(data, i, 0, n - 1) else "no", end=' ')

"""
5
8 3 7 9 2
3
5 7 9
"""