import sys

input = sys.stdin.readline

data = list(input().rstrip())

p_cnt = data.count('o')
l_cnt = data.count('-')

print("YES" if p_cnt == 0 or l_cnt % p_cnt == 0 else "NO")
