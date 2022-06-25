import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    memo = set()
    smemo = set()
    flag = True
    for i in range(n):
        if b[i] != 0:
            memo.add(a[i] - b[i])
        else:
            smemo.add(a[i])

        if a[i] < b[i]:
            flag = False
            break

        if len(memo) > 1:
            flag = False
            break

    if smemo and memo:
        if max(smemo) > memo.pop():
            flag = False
    print("YES" if flag else "NO")