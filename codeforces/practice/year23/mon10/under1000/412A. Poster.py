import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = input().rstrip()

if k - 1 < n - k:
    for _ in range(k - 1):
        print("LEFT")
    print("PRINT " + data[0])
    for i in range(1, n):
        print("RIGHT")
        print("PRINT " + data[i])

else:
    for _ in range(n - k):
        print("RIGHT")
    print("PRINT " + data[n - 1])
    for i in range(n - 2, -1, -1):
        print("LEFT")
        print("PRINT " + data[i])

