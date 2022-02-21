import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
cntn = len([i for i in data if i < 0])
cntp = n - cntn - data.count(0)

if max(cntn, cntp) < (n + 1) // 2:
    print(0)
else:
    print(-1 if cntn > cntp else 1)
