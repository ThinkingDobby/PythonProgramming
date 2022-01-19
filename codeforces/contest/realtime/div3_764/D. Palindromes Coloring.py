import collections

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(input())
    cnt = collections.Counter(data)
    even = 0
    rest = 0
    for i in cnt.keys():
        even += cnt[i] // 2
        rest += 1 if cnt[i] % 2 == 1 else 0

    each = (even // k) * 2
    tmp = 2 * (even % k) + rest
    each += 1 if tmp // k >= 1 else 0
    print(max(each, 1))