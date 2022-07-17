import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, q = map(int, input().split())
    data = sorted(map(int, input().split()))
    memo = [0 for _ in range(n)]
    memo[0] = data[-1]
    for i in range(1, n):
        memo[i] = memo[i - 1] + data[-(i + 1)]

    queries = sorted([[i, int(input())] for i in range(q)], key=lambda x: x[1])

    qnow = 0
    ans = []
    chk = True
    for i in range(n):
        while memo[i] >= queries[qnow][1]:
            ans.append([queries[qnow][0], i + 1])
            qnow += 1
            if qnow >= q:
                chk = False
                break
            if i == n - 1 and memo[i] < queries[qnow][1]:
                chk = False
                break
        if not chk:
            break

    for i in range(qnow, q):
        ans.append([queries[i][0], -1])

    for i in sorted(ans):
        print(i[1])

