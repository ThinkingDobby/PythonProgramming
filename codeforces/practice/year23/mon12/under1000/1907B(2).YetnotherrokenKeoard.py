import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = list(input().rstrip())

    lower_idx_queue = collections.deque()
    upper_idx_queue = collections.deque()

    for i in range(len(data)):
        if data[i] == 'b':
            data[i] = ''
            if lower_idx_queue:
                idx = lower_idx_queue.pop()
                data[idx] = ''
        elif data[i] == 'B':
            data[i] = ''
            if upper_idx_queue:
                idx = upper_idx_queue.pop()
                data[idx] = ''

        elif data[i].islower():
            lower_idx_queue.append(i)
        else:
            upper_idx_queue.append(i)

    print(''.join(data))
