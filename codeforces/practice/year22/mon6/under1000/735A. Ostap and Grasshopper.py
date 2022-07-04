import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = input().rstrip()

g_loc = data.find('G')
i_loc = data.find('T')

if abs(g_loc - i_loc) % k == 0:
    ans = True
    if g_loc < i_loc:
        for i in range(g_loc, i_loc, k):
            if data[i] == '#':
                ans = False
                break
    else:
        for i in range(i_loc, g_loc, k):
            if data[i] == '#':
                ans = False
                break
    print("YES" if ans else "NO")
else:
    print("NO")