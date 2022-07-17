import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()
    sdata = set(data)

    memo = {i:-1 for i in sdata}

    ans = True
    for i in range(len(data)):
        tmp = memo[data[i]]
        if i - tmp > len(sdata):
            ans = False
            break
        else:
            memo[data[i]] = i

    for i in memo.keys():
        if len(data) - memo[i] > len(sdata):
            ans = False
            break

    print("YES" if ans else "NO")

