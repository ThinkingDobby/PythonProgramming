import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()

    chk = set()
    ans = False
    i = 0
    while i < n - 1:
        tmp = data[i:i + 2]
        if tmp in chk:
            ans = True
        else:
            if i < n - 2 and data[i] == data[i + 1] and data[i + 1] == data[i + 2]:
                i += 1
            chk.add(tmp)
        i += 1

    print("YES" if ans else "NO")
