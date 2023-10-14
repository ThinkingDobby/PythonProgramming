import sys

input = sys.stdin.readline

data = sorted(map(int, input().split()))
if data[3] < data[2] + data[1] or data[2] < data[1] + data[0]:
    print("TRIANGLE")
elif data[3] == data[2] + data[1] or data[2] == data[1] + data[0]:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")