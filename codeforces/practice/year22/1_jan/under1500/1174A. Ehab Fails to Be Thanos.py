n = int(input())
data = list(map(int, input().split()))
if len(set(data)) == 1:
    print(-1)
else:
    head = data[:n]
    tail = data[n:]

    if sum(head) == sum(tail):
        min_idx = head.index(min(head))
        max_idx = tail.index(max(tail)) + n
        data[min_idx], data[max_idx] = data[max_idx], data[min_idx]
        print(*data)
    else:
        print(*data)