import sys

sys.stdin = open("sample_input.txt", "r")


def solve():
    result = ""
    for t in range(int(input())):
        n, m = map(int, input().split())
        data = [list(map(int, input().split())) for _ in range(n)]
        homes = []

        for i in range(n):
            for j in range(n):
                if data[i][j] == 1:
                    homes.append([i, j])

        ans = -1
        for i in range(n):
            for j in range(n):
                dist_cnt = [0] * (n * 2 + 1)

                for a, b in homes:
                    dist_cnt[abs(a - i) + abs(b - j) + 1] += 1

                for l in range(1, n * 2 + 1):
                    dist_cnt[l] += dist_cnt[l - 1]

                for k in range(n * 2 + 1):
                    cost = k * k + (k - 1) * (k - 1)
                    if cost <= dist_cnt[k] * m:
                        ans = max(ans, dist_cnt[k])

        result += f"#{t + 1} {ans}\n"

    return result


result = solve()
print(result)

with open("sample_output.txt", "r") as file:
    output = file.read()

if output.rstrip() == result.rstrip():
    print("Correct")
else:
    print("Wrong")