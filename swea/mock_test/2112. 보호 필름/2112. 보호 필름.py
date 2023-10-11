# TLE

import collections
import itertools
import sys

sys.stdin = open("sample_input.txt", "r")


def print_list(data):
    for i in data:
        for j in i:
            print(j, end=' ')
        print()
    print("----------")


def check(data, d, w, k, a_lines, b_lines):
    memo = [[-1] * w for _ in range(d)]

    for i in range(d):
        for j in range(w):
            if i in a_lines:
                memo[i][j] = 0
            elif i in b_lines:
                memo[i][j] = 1
            else:
                memo[i][j] = data[i][j]

    # print(a_lines, b_lines)
    # print_list(memo)

    for j in range(w):
        chk = False
        cnts = collections.defaultdict(int)
        cnts[memo[0][j]] += 1

        for i in range(1, d):
            if memo[i - 1][j] != memo[i][j]:
                cnts[memo[i][j]] = 1
                cnts[memo[i - 1][j]] = 0
            else:
                cnts[memo[i][j]] += 1
                if max(cnts.values()) >= k:
                    chk = True
                    break

        if not chk:
            return False

    return True


def solve():
    result = ""
    
    for t in range(int(input())):
        d, w, k = map(int, input().split())
        data = [list(map(int, input().split())) for _ in range(d)]
        
        ans = check(data, d, w, k, {}, {})
        cnt = 0

        for i in range(max(d, k) + 1):
            for lines in itertools.combinations(range(d), i):
                # print(lines)
                for j in range(i + 1):
                    for a_lines in itertools.combinations(lines, j):
                        if check(data, d, w, k, set(a_lines), set(lines) - set(a_lines)):
                            cnt = i
                            ans = True
                            break
                    if ans: break
                if ans: break
            if ans: break

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
