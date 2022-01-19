n = int(input())
store = sorted(map(int, input().split()))
m = int(input())
guest = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            return mid

    return None


for i in guest:
    if binary_search(store, i, 0, n - 1):
        print("yes", end=' ')
    else:
        print("no", end=' ')