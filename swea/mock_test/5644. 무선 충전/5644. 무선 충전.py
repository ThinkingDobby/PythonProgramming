import sys

sys.stdin = open("sample_input.txt", "r")

dirs = {0: (0, 0), 1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}


def solve():
    result = ""

    for t in range(int(input())):
        m, n = map(int, input().split())    # 총 이동 시간, BC 수
        a = [0] + list(map(int, input().split()))
        b = [0] + list(map(int, input().split()))

        bc_info = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: -x[3])    # x, y, 범위, 성능

        a_now = [1, 1]
        b_now = [10, 10]

        cnt = 0
        for time in range(m + 1):
            a_bc = []
            b_bc = []

            a_now[0] += dirs[a[time]][0]
            a_now[1] += dirs[a[time]][1]
            b_now[0] += dirs[b[time]][0]
            b_now[1] += dirs[b[time]][1]

            # print(time, a_now, b_now)

            for i in range(n):
                bc = bc_info[i]
                if abs(a_now[0] - bc[0]) + abs(a_now[1] - bc[1]) <= bc[2]: a_bc.append(i)
                if abs(b_now[0] - bc[0]) + abs(b_now[1] - bc[1]) <= bc[2]: b_bc.append(i)

            # print(time, a_bc, b_bc)

            chk = set(a_bc) & set(b_bc)
            if chk:
                if a_bc[0] == b_bc[0]:
                    case = [bc_info[a_bc[0]][3]]
                    if len(a_bc) > 1: case.append(bc_info[a_bc[1]][3] + case[0])
                    if len(b_bc) > 1: case.append(bc_info[b_bc[1]][3] + case[0])
                    cnt += max(case)
                else:
                    cnt += bc_info[a_bc[0]][3]
                    cnt += bc_info[b_bc[0]][3]
            else:
                if a_bc: cnt += bc_info[a_bc[0]][3]
                if b_bc: cnt += bc_info[b_bc[0]][3]

        result += f"#{t + 1} {cnt}\n"

    return result


result = solve()
print(result)

with open("sample_output.txt", "r") as file:
    output = file.read()

if result.rstrip() == output.rstrip():
    print("Correct")
else:
    print("Wrong")
