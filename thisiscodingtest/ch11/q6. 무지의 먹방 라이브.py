def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    else:
        s = 0
        memo = {}
        for i in food_times:
            memo[i] = memo[i] + 1 if i in memo else 1
        smemo = sorted(list(memo.items()))
        now_len = len(food_times)
        i = 0
        while True:
            # print('s:', s, 'now_len:', now_len, 'smemo[i]:', smemo[i])
            tmp = s + now_len * (smemo[i][0] - (0 if i == 0 else smemo[i - 1][0]))
            if tmp >= k + 1:
                break
            s = tmp
            now_len -= smemo[i][1]
            i += 1

        # print(now_len, s, smemo[i], k - s, i)
        cnt = (k - s + 1 + now_len - 1) % now_len + 1
        # print(cnt)
        now = 0
        for j in range(len(food_times)):
            # print(now, cnt)
            if food_times[j] >= smemo[i][0]:
                now += 1
            if now == cnt:
                ans = j
                break

        return ans + 1


while True:
    print(solution([4, 3, 2], int(input())))