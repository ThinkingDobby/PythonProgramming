import sys

input = sys.stdin.readline


x = input().rstrip()
y = input().rstrip()

chk = True
for i in range(len(x)):
    if ord(x[i]) < ord(y[i]):
        chk = False

print(y if chk else -1)