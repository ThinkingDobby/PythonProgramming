from collections import *

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    ans = deque([data[0]])  # 리스트 뒷 부분에 요소 추가 시 시간 복잡도 애매할 때는 deque 사용
    for i in range(1, n):
        if data[i] <= ans[0]:
            ans.insert(0, data[i])
        else:
            ans.append(data[i])
    print(*ans)