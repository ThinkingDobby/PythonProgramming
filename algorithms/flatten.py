# itertools.chain 사용
import itertools

lst = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]

f_lst = list(itertools.chain(*lst))
print(f_lst)


# 리스트 내포 사용
def flatten(lst):
    return [x for y in lst for x in y]

# 리스트 내포 내의 이중 for 문: 좌 각각 요소에 우 for 문 수행 된다고 생각
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
f_lst = flatten(lst)
print(f_lst)