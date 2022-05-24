import sys
import itertools

input = sys.stdin.readline

data = [chr(i) for i in range(97, 123)]
ans = list(map(lambda x: x[0] + x[1], list(itertools.permutations(data, 2))))

for _ in range(int(input())):
    data = input().rstrip()
    print(ans.index(data) + 1)