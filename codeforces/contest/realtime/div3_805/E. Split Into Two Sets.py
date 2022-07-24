# WA
# Edge Coloring 문제 - 보류

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    dict_f = dict()
    dict_s = dict()
    ans = True
    for i in range(n):
        a, b = sorted(map(int, input().split()))
        if a == b:
            ans = False

        if a in dict_f:
            if b in dict_f:
                if dict_f[a] == dict_f[b]:
                    ans = False
            if b in dict_s:
                if dict_f[a] == dict_s[b]:
                    ans = False
            if len(dict_f[a]) == 2:
                ans = False
            dict_f[a].add(b)
        else:
            dict_f[a] = {b, }
        if b in dict_s:
            if a in dict_f:
                if dict_s[b] == dict_f[a]:
                    ans = False
            if a in dict_s:
                if dict_s[b] == dict_s[a]:
                    ans = False
            if len(dict_s[b]) == 2:
                ans = False
            dict_s[b].add(a)
        else:
            dict_s[b] = {a, }

    print("YES" if ans else "NO")

    #     if a not in set_a and b not in set_a:
    #         set_a.add(a)
    #         set_a.add(b)
    #     else:
    #         set_b.add(a)
    #         set_b.add(b)
    #
    # if len(set_a) + len(set_b) == n * 2:
    #     print("YES")
    # else:
    #     print("NO")
