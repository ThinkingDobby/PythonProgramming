for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    even_cnt = 0
    odd_cnt = 0
    odd_ans = []

    for i in range(n):
        if data[i] % 2 == 0:
            even_cnt += 1
            print(1)
            print(i + 1)
            break
        else:
            odd_cnt += 1
            odd_ans.append(i + 1)
            if odd_cnt == 2:
                print(2)
                print(*odd_ans)
                break

    if even_cnt == 0 and odd_cnt < 2:
        print(-1)