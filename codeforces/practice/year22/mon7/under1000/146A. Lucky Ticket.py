import sys

input = sys.stdin.readline

n = int(input())
data = input().rstrip()
f = data[:n // 2].count('4')
s = data[n // 2:].count('4')

if set(data) - {'4', '7'} != set():
    print("NO")
else:
    print("YES" if f == s else "NO")
