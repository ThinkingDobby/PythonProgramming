def solution(n, words):
    ans = [0, 0]

    memo = set([words[0]])
    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0] or words[i] in memo:
            ans[0] = i % n + 1
            ans[1] = i // n + 1
            break

        memo.add(words[i])

    return ans