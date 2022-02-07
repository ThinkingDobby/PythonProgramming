import math

a = 3
b = 2
cnt = math.perm(a, b)
print(cnt)
# 순열 개수 계산
# a개에서 b개를 뽑아 (순서를 고려해) 나열하는 경우의 수


import itertools

data = ['a', 'b', 'c']
ans = list(itertools.permutations(data, 2))
print(ans)
# 순열 모든 경우 계산
# a개에서 b개를 뽑아 (순서를 고려해) 나열하는 모든 경우

ans = list(itertools.product(data, repeat=2))
print(ans)
# 중복순열 모든 경우 계산
