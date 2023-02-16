import sys

input = sys.stdin.readline


def check(t):
    h = t // 60
    m = t % 60

    return h // 10 == 7 or h % 10 == 7 or m // 10 == 7 or m % 10 == 7


x = int(input())

data = input().split()
time = int(data[0]) * 60 + int(data[1])

cnt = 0
while not check(time):
    cnt += 1
    time -= x
    if time <= 0:
        time += 24 * 60

print(cnt)

