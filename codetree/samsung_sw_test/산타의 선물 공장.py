# TLE

# 해결 방법:
# 각 큐의 시작과 끝 요소 id를 딕셔너리에 저장
# 큐의 각 요소의 앞, 뒤 요소 id를 딕셔너리에 저장
# 탐색, 삭제 등 O(1)에 가능해짐

import collections
import sys

input = sys.stdin.readline


def check_belt_parent(belt_parent, x):
    if belt_parent[x] != x:
        belt_parent[x] = check_belt_parent(belt_parent, belt_parent[x])
    return belt_parent[x]


q = int(input())
f_data = list(map(int, input().split()))
n = f_data[1]
m = f_data[2]

belt_num = dict()   # 각 물건의 벨트 번호
item_weight = dict()
belts = [collections.deque() for _ in range(m)] # 각 벨트 - 물건 번호 저장
belt_parent = [i for i in range(m)]    # 합쳐진 벨트 저장 (벨트 고장 판단)

for i in range(3, 3 + n):
    belt_num[f_data[i]] = (i - 3) // (n // m)
    item_weight[f_data[i]] = f_data[i + n]
    belts[(i - 3) // (n // m)].append(f_data[i])

for _ in range(q - 1):
    data = list(map(int, input().split()))

    if data[0] == 200:
        w_max = data[1]
        s = 0

        for belt_now in range(m):
            if belt_parent[belt_now] == belt_now:   # 고장 안난 벨트에 대해
                if belts[belt_now]:
                    now = belts[belt_now].popleft()
                    if item_weight[now] <= w_max:
                        s += item_weight[now]
                        belt_num[now] = -1
                    else:
                        belts[belt_now].append(now) # 무게 크면 맨 뒤에 삽입
        print(s)

    elif data[0] == 300:
        r_id = data[1]

        if r_id not in belt_num or belt_num[r_id] == -1:    # 없거나 이미 빠진 경우
            print(-1)
        else:
            belt_now = check_belt_parent(belt_parent, belt_num[r_id])
            belts[belt_now].remove(r_id)
            belt_num[r_id] = -1

            print(r_id)

    elif data[0] == 400:
        f_id = data[1]
        if f_id not in belt_num or belt_num[f_id] == -1:
            print(-1)
        else:
            belt_now = check_belt_parent(belt_parent, belt_num[f_id])
            f_id_idx = belts[belt_now].index(f_id)

            belts[belt_now] = collections.deque(list(belts[belt_now])[f_id_idx:] + list(belts[belt_now])[:f_id_idx])

            print(belt_now + 1)

    elif data[0] == 500:
        b_num = data[1] - 1

        if belt_parent[b_num] != b_num: # 이미 고장난 경우
            print(-1)
        else:
            new = -1
            for i in range(1, m):
                new = (b_num + i) % m
                if check_belt_parent(belt_parent, new) == new:  # 고장 안 난 벨트 탐색
                    break

            belts[new] += belts[b_num]
            belt_parent[b_num] = new

            print(b_num + 1)

