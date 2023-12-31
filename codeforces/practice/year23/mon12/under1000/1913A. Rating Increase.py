import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()

    ans = -1
    for i in range(1, len(data)):
        f = data[:i]
        s = data[i:]

        if len(str(int(f))) + len(str(int(s))) == len(data) and int(f) < int(s):
            ans = i
            break

    if ans == -1:
        print(-1)
    else:
        print(data[:ans], data[ans:])