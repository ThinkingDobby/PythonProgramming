for _ in range(int(input())):
    n = int(input())
    s = list(input())
    t = list(input())
    memo = [ord(s[i]) - ord(t[i]) for i in range(n)]
    cnt = memo.count(0)

    if cnt == n:
        print("Yes")
    elif n - cnt == 2:
        if len(set(memo) - {0}) == 1:
            tmp = []
            for i in range(n):
                if memo[i] != 0:
                    tmp.append(i)
            if s[tmp[0]] == s[tmp[1]]:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
