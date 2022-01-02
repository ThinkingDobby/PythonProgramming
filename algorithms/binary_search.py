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


ex = [1, 1, 1, 2, 2, 2, 3, 4, 4, 4]
print(binary_search(ex, 2, 0, len(ex) - 1))
print(lower_bound(ex, 2, 0, len(ex) - 1))
print(upper_bound(ex, 2, 0, len(ex) - 1))
