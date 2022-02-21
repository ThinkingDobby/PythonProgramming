import sys

prev = sys.maxsize
flag = True

for _ in range(int(input())):
    w, h = map(int, input().split())
    if prev >= max(w, h):
        prev = max(w, h)
    elif prev >= min(w, h):
        prev = min(w, h)
    else:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")