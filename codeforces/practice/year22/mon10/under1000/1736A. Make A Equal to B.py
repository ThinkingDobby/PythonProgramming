import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt1_a = len([i for i in a if i == 1])
    cnt1_b = len([i for i in b if i == 1])
    if cnt1_a == cnt1_b:
        print(0 if all([a[i] == b[i] for i in range(n)]) else 1)
    else:
        print(min(abs(cnt1_a - cnt1_b) + 1, len([1 for i in range(n) if a[i] != b[i]])))
