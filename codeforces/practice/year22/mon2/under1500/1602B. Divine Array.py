import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    q = int(input())
    queries = sorted([list(map(int, input().split()))[::-1] + [i] for i in range(q)])

    prev = data[:]
    cnts = dict(collections.Counter(data))
    cnt = 0
    qidx = 0

    ans = []
    while True:
        while qidx < q and queries[qidx][0] == cnt:
            ans.append([prev[queries[qidx][1] - 1], queries[qidx][2]])
            qidx += 1
        if qidx >= q:
            break

        cnts = dict(collections.Counter(data))
        for i in range(n):
            data[i] = cnts[prev[i]]

        if prev == data:
            while qidx < q:
                ans.append([prev[queries[qidx][1] - 1], queries[qidx][2]])
                qidx += 1
            break

        prev = data[:]
        cnt += 1

    ans.sort(key=lambda x: x[1])
    for i in range(q):
        print(ans[i][0])
