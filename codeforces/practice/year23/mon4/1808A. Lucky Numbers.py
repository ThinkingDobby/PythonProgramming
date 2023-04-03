import sys

input = sys.stdin.readline

for _ in range(int(input())):
    l, r = list(map(int, input().split()))

    chk = False
    ans = -1
    max_v = -1

    for i in range(l, r + 1):
        memo = set(map(int, str(i)))
        tmp = max(memo) - min(memo)
        
        if tmp > max_v:
            max_v = tmp
            ans = i
            if max_v == 9:
                break

    print(ans)



            
            
