import sys

input = sys.stdin.readline

ft = 0
st = 0
fa = 0
sa = 0

for _ in range(int(input())):
    t, x, y = map(int, input().split())
    if t == 1:
        ft += x + y
        fa += x
    else:
        st += x + y
        sa += x

print("LIVE" if fa >= ft // 2 else "DEAD")
print("LIVE" if sa >= st // 2 else "DEAD")