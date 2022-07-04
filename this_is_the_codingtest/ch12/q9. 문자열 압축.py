def solution(s):
    mv = len(s)
    for i in range(1, (len(s) + 1) // 2 + 1):
        cnt = 0
        tmp = 1
        for j in range(i, len(s) - i + 1, i):
            if s[j - i:j] != s[j:j + i]:
                if tmp == 1:
                    cnt += i
                else:
                    cnt += i + len(str(tmp))
                    tmp = 1
            else:
                tmp += 1

        if tmp == 1:
            cnt += i
        else:
            cnt += i + len(str(tmp))

        mv = min(mv, cnt + len(s) % i)

    return mv


print(solution(input()))

