for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    m = int(input())
    q = list(map(int, input().split()))

    p_even = [i for i in p if i % 2 == 0]
    q_even = [i for i in q if i % 2 == 0]

    e = len(p_even) * len(q_even)
    o = (n - len(p_even)) * (m - len(q_even))

    print(e + o)