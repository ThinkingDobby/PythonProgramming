import sys

input = sys.stdin.readline


def binary_search(data, target, _l, _r):
    l = _l
    r = _r

    while l <= r:
        mid = (l + r) // 2
        if data[mid] < target:
            l = mid + 1
        elif data[mid] > target:
            r = mid - 1
        else:
            return mid


for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    a_memo = [0] * n
    b_memo = [0] * n
    a_memo[0] = data[0]
    b_memo[0] = data[-1]

    for i in range(1, n):
        a_memo[i] += a_memo[i - 1] + data[i]
        b_memo[i] += b_memo[i - 1] + data[-(i + 1)]

    ans = 0
    for i in range(n - 1):
        tmp = a_memo[i]
        idx = binary_search(b_memo, tmp, 0, n - 2 - i)
        # print(i, idx, n - 2 - i)
        if idx is not None and b_memo[idx] == a_memo[i]:
            ans = i + idx + 2

    print(ans)


