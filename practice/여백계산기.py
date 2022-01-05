t, n, mn, r = map(int, input("너비 개수 여백개수 여백범위: ").split())

print("너비 여백:")
for i in range(r):
    if (t - i * mn) % n == 0:
        print((t - i * mn) // n, i)
