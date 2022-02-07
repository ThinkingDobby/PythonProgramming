n = int(input())
memo = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]
data = list(input())

for i in memo:
    if len(i) == n:
        flag = True
        for j in range(n):
            if data[j] != '.' and i[j] != data[j]:
                flag = False
                break
        if flag:
            print(i)
            break
