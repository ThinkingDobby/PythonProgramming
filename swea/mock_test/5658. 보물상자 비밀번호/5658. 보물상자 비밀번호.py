import sys

sys.stdin = open("sample_input.txt", "r")


def solve():
    result = ""

    for t in range(int(input())):
        n, k = map(int, input().split())
        data = input().rstrip()

        side_len = n // 4
        data = data[-(side_len - 1):] + data

        memo = set()
        for i in range(len(data) - (side_len - 1)):
            memo.add(int(data[i:i + side_len], 16))

        ans = sorted(memo, reverse=True)[k - 1]
        result += f"#{t + 1} {ans}\n"

    return result


result = solve()
print(result)

with open("sample_output.txt", "r") as file:
    output = file.read()

if result.rstrip() == output:
    print("Correct")
else:
    print("Wrong")