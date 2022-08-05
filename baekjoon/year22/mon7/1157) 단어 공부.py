import sys

input = sys.stdin.readline

memo = [0 for _ in range(26)]
data = input().rstrip()

for i in data:
    memo[ord(i.lower()) - 97] += 1

smemo = sorted(memo)
if len(data) > 1:
    if smemo[-1] == smemo[-2]:
        print('?')
    else:
        print(chr(memo.index(max(memo)) + 65))
else:
    print(data[0].upper())