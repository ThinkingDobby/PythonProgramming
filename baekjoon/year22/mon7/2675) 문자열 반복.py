num_test = int(input())

for i in range(num_test):
    a = list(input().split())
    a[0] = int(a[0])
    a[1] = list(a[1])
    for j in range(len(a[1])):
        print(a[1][j] * a[0] , end='')
    print()