for _ in range(int(input())):
    data = input()
    memo = [0] * 26

    chk = set()
    for i in range(len(data)):
        tmp = ord(data[i]) - 97
        if memo[tmp] == 1:
            chk.add(data[i])
        memo[tmp] += 1

    print("".join(list(chk)) * 2 + "".join(list(set(data) - chk)))