# TLE

import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()

    lower_idx_queue = collections.deque()
    lower_chr_queue = collections.deque()

    upper_idx_queue = collections.deque()
    upper_chr_queue = collections.deque()

    for i in range(len(data)):
        if data[i] == 'b':
            if lower_idx_queue:
                lower_idx_queue.pop()
                lower_chr_queue.pop()
        elif data[i] == 'B':
            if upper_idx_queue:
                upper_idx_queue.pop()
                upper_chr_queue.pop()
        elif data[i].islower():
            lower_idx_queue.append(i)
            lower_chr_queue.append(data[i])
        else:
            upper_idx_queue.append(i)
            upper_chr_queue.append(data[i])

    tmp = list(zip(lower_idx_queue, lower_chr_queue)) + list(zip(upper_idx_queue, upper_chr_queue))
    print(''.join(map(lambda x: x[1], sorted(tmp))))
