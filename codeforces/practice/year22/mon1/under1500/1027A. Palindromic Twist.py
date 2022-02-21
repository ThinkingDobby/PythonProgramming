for _ in range(int(input())):
    n = int(input())
    data = list(input())
    memo = ([abs(ord(data[i]) - ord(data[-(i + 1)])) for i in range(n // 2)])
    if max(memo) <= 2 and 1 not in memo:
        print("YES")
    else:
        print("NO")