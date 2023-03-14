import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    data = input().rstrip()
    counter = collections.Counter(data)

    rest = 0
    cnt = 0
    for i in range(26):
        a = 0 if chr(i + 97) not in counter else counter[chr(i + 97)]
        b = 0 if chr(i + 65) not in counter else counter[chr(i + 65)]

        cnt += min(a, b)
        rest += (max(a, b) - min(a, b)) // 2

    print(cnt + min(rest, k))
