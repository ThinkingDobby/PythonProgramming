memo = [1, 2, 3, 4, 6, 12]

for _ in range(int(input())):
    data = list(input())
    
    ans = []
    for i in memo:
        for j in range(12 // i):
            flag = True
            for k in range(j, 12, 12 // i):
                if data[k] != 'X':
                    flag = False
            if flag:
                ans.append(i)
                break

    print(len(ans), end=' ')
    if len(ans) != 0:
        for i in ans:
            print(str(i) + 'x' + str(12 // i), end=' ')

    print()