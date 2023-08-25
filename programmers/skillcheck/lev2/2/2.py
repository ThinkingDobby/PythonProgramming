def solution(n, left, right):
    ans = [0] * (right - left + 1)

    for i in range(left, right + 1):
        row = i // n + 1
        col = i % n

        if col < row:
            ans[i - left] = row
        else:
            ans[i - left] = col + 1

    return ans

ans = solution(10000000, 1, 100000)
print(ans)