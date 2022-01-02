for t in range(int(input())):
    a = input()
    if a[:int(len(a) / 2)] == a[int(len(a) / 2):]:
        print("YES")
    else:
        print("NO")