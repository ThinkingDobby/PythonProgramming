def solution(players, callings):
    name = dict()
    rank = dict()

    for i in range(len(players)):
        name[players[i]] = i
        rank[i] = players[i]

    for target in callings:
        name[target] -= 1
        tmp = rank[name[target]]
        name[tmp] += 1

        rank[name[target]] = target
        rank[name[target] + 1] = tmp

    answer = [rank[i] for i in range(len(players))]
    return answer

