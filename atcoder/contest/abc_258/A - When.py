import sys

input = sys.stdin.readline

k = int(input())
print("%02d" % (21 + k // 60), end='')
print(':', end='')
print("%02d" % (k % 60))