n, m = map(int, input().split())
data = list(map(int, input().split()))

left = 0
right = max(data)
while left < right:
    mid = (left + right) // 2
    now = sum([i - mid if i > mid else 0 for i in data])
    if m <= now:    # 조건을 적절히 변경해 풀이
        left = mid + 1  # 고정
    else:
        right = mid

print(right - 1)