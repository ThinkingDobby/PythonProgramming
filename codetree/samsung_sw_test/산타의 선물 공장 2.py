# unsolved

import collections
import sys

input = sys.stdin.readline


def init_factory(data, m, item_count, prev, next, head, tail):
    belt_items = collections.defaultdict(list)
    for i in range(m):
        belt_items[data[i] - 1].append(i + 1)

    for belt_num in belt_items:
        now_items = belt_items[belt_num]
        item_count[belt_num] = len(now_items)

        head[belt_num] = now_items[0]
        tail[belt_num] = now_items[-1]

        for i in range(1, item_count[belt_num]):
            next[now_items[i - 1]] = now_items[i]
            prev[now_items[i]] = now_items[i - 1]


def move_all(data, item_count, prev, next, head, tail):
    m_src = data[0] - 1
    m_dst = data[1] - 1

    if head[m_src] != 0:
        next[tail[m_src]] = head[m_dst]
        prev[head[m_dst]] = tail[m_src]

        head[m_dst] = head[m_src]
        head[m_src] = 0
        tail[m_src] = 0

        item_count[m_dst] += item_count[m_src]
        item_count[m_src] = 0

    print(item_count[m_dst])


q = int(input())
data = list(map(int, input().split()))

n = data[1] # 벨트 수
m = data[2] # 물건 수

item_count = [0] * n
prev = collections.defaultdict(int)
next = collections.defaultdict(int)
head = collections.defaultdict(int)
tail = collections.defaultdict(int)

init_factory(data[3:], m, item_count, prev, next, head, tail)

for _ in range(q - 1):
    data = list(map(int, input().split()))

    if data[0] == 200:
        move_all(data, item_count, prev, next, head, tail)

