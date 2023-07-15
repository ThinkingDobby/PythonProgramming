h, w = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(h)]
for j in range(w):
    for i in range(h):
        print(data[i][j], end=' ')
    print()