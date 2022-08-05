import collections

# 기본값을 지정할 수 있는 딕셔너리

# 기본값이 0인 딕셔너리
int_dict = collections.defaultdict(int)
print(int_dict['a'])

# 기본값이 빈 리스트인 딕셔너리
list_dict = collections.defaultdict(list)
print(list_dict[1])
