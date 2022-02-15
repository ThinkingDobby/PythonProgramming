import itertools

l, c = map(int, input().split())
data = list(input().split())

vow = list(set(data) & {'a', 'e', 'i', 'o', 'u'})
con = list(set(data) - {'a', 'e', 'i', 'o', 'u'})

ans = []
for i in range(1, min(l - 2, len(vow)) + 1):
    a = list(itertools.combinations(vow, i))
    b = list(itertools.combinations(con, l - i))
    for j in a:
        for k in b:
            ans.append(''.join(sorted(j + k)))

ans.sort()
for i in ans:
    print(i)

"""
4 6
a t c i s w
"""