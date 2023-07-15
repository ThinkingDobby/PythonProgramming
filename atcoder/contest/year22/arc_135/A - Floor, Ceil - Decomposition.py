mod = 998244353

n = int(input())

memo = {}


def func(n):
    if n < 5:
        return n

    a = (n + 1) // 2
    b = n // 2

    if a in memo:
        tmpa = memo[a]
    else:
        memo[a] = func(a)
        tmpa = memo[a]

    if b in memo:
        tmpb = memo[b]
    else:
        memo[b] = func(b)
        tmpb = memo[b]

    return tmpa * tmpb % mod


print(func(n))