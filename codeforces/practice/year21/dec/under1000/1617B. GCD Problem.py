for t in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print(n // 2 - 1, n // 2, 1)    # 연속된 두 수의 최대공약수는 반드시 1
    else:
        tmp = (n - 1) // 2
        if tmp % 2 == 0:
            print(tmp - 1, tmp + 1, 1)  # 연속된 두 홀수의 최대공약수는 반드시 1
        else:
            print(tmp - 2, tmp + 2, 1)  # 두 홀수 a - 2와 a + 2의 최대공약수는 반드시 1
