for _ in range(int(input())):
    n, k = map(int, input().split())
    if n % 2 == 0 or k == 1:
        print("YES")
        odd = 1
        even = 2
        for i in range(n):
            for _ in range(k):
                if i % 2 == 0:
                    print(odd, end=' ')
                    odd += 2
                else:
                    print(even, end=' ')
                    even += 2
            print()
    else:
        print("NO")