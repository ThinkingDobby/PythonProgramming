import collections

k = int(input())
data = list(input())
cdata = dict(collections.Counter(data))
flag = True

for i in cdata.values():
    if i % k != 0:
        flag = False
        break

if not flag:
    print(-1)
else:
    ans = ''
    for i in cdata.keys():
        ans += i * (cdata[i] // k)
    print(ans * k)
