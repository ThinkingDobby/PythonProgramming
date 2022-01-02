def solution(N, number):
    memo = []

    for i in range(1, 9):
        now = {int(str(N) * i)}
        for j in range(0, i - 1):
            for x in memo[j]:
                for y in memo[-j - 1]:
                    now.add(x - y)
                    now.add(x + y)
                    now.add(x * y)
                    if y != 0:
                        now.add(x // y)
        if number in now:
            return i
        memo.append(now)
    return -1


print(solution(int(input()), int(input())))
