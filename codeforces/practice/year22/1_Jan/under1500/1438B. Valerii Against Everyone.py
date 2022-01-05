import sys
inp = sys.stdin.readline

for _ in range(int(inp())):
    n = int(inp())
    data = sorted(map(int, inp().split()))
    flag = False
    for i in range(1, n):
        if data[i] == data[i - 1]:
            flag = True
            break

    if flag:
        print("YES")
    else:
        print("NO")