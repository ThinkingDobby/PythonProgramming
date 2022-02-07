import math

a = 3
b = 2
cnt = math.comb(a, b)
print(cnt)
# 조합 개수 계산
# a개에서 b개를 뽑아 순서를 고려하지 않고 나열하는 경우의 수


import itertools

data = ['a', 'b', 'c']
ans = list(itertools.combinations(data, 2))
print(ans)
# 조합 모든 경우 계산
# a개에서 b개를 뽑아 순서를 고려하지 않고 나열하는 모든 경우

ans = list(itertools.combinations_with_replacement(data, 2))
print(ans)
# 중복조합 모든 경우 계산
