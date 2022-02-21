trump = input()
a, b = input().split()

rank = ["6", "7", "8", "9", "T", "J", "Q", "K", "A"]

if a[1] == b[1]:
    if rank.index(a[0]) > rank.index(b[0]):
        print("YES")
    else:
        print("NO")
else:
    if a[1] == trump and b[1] != trump:
        print("YES")
    else:
        print("NO")