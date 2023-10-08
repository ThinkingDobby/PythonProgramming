def binary_search(data, target, _l, _r):
    l = _l
    r = _r

    while l <= r:
        mid = (l + r) // 2
        if data[mid] < target:
            l = mid + 1
        elif data[mid] > target:
            r = mid - 1
        else:
            return mid


def lower_bound(data, target, _l, _r):
    l = _l
    r = _r

    while l < r:
        mid = (l + r) // 2
        if data[mid] < target:
            l = mid + 1
        else:
            r = mid

    return r


def upper_bound(data, target, _l, _r):
    l = _l
    r = _r

    while l < r:
        mid = (l + r) // 2
        if data[mid] <= target:
            l = mid + 1
        else:
            r = mid

    return r


ex = [1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 6, 8]
print(binary_search(ex, 2, 0, len(ex) - 1))
# 찾는 값 없으면 None 반환

# target에 해당하는 가장 작은 인덱스 반환
print(lower_bound(ex, 2, 0, len(ex) - 1))
# target에 해당하는 가장 큰 인덱스 + 1 반환
print(upper_bound(ex, 2, 0, len(ex) - 1))

# bisect 라이브러리 이용 가능
import bisect
print(bisect.bisect_left(ex, 2))
print(bisect.bisect_right(ex, 2))

# 리스트 내에 찾는 값 없으면 그 값보다 큰 첫번째 요소 인덱스 반환 - 공통 특징
