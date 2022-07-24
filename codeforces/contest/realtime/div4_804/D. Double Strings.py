# us

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = [input().rstrip() for _ in range(n)]
    set_data = set(data)
    s_data = sorted(data, key=lambda x: len(x))

    ans = set()
    for i in range(n):
        for j in range(i, n):
            tmp = s_data[i] + s_data[j]
            if tmp in set_data:
                ans.add(tmp)
                set_data.remove(s_data[i] + s_data[j])
            tmp2 = s_data[j] + s_data[i]
            if tmp2 in set_data:
                ans.add(tmp2)
                set_data.remove(s_data[j] + s_data[i])
            if s_data[j] in set_data:
                set_data.remove(s_data[j])
        if s_data[i] in set_data:
            set_data.remove(s_data[i])

    for i in range(n):
        if data[i] in ans:
            print(1, end='')
        else:
            print(0, end='')
    print()