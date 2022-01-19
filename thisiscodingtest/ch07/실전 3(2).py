n, m = map(int, input().split())
data = list(map(int, input().split()))

left = 0
right = max(data)
ans = -1
while left <= right:
    mid = (left + right) // 2
    now = sum([i - mid if i > mid else 0 for i in data])
    if m <= now:
        left = mid + 1
    else:
        right = mid - 1
        ans = right     # 같은 결과 내는 경우에 대해 가장 큰 값이 저장됨

print(ans)