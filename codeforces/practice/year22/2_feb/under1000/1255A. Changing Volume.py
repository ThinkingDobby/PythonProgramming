for _ in range(int(input())):
    a, b = map(int, input().split())
    cnt = abs(a - b) // 5
    cnt += (abs(a - b) % 5) // 2
    cnt += (abs(a - b) % 5) % 2
    print(cnt)
