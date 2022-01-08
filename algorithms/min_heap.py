import heapq

min_heap = [5, 3, 6, 1, 2]

heapq.heapify(min_heap)  # 리스트를 최소 힙 형태로 변경
print(min_heap)
#         1
#     2       6
# 3   5
# 느슨한 정렬 상태: 부모 노드 값이 자식 노드 값보다 작음

heapq.heappush(min_heap, 4)  # 최소 힙에 요소 추가
print(min_heap)

print(heapq.heappop(min_heap))  # 최솟값 pop
print(min_heap)

# 주요 문제: abc_234D


# 최대 힙 - 기본적으로 지원x, 응용 필요: 우선순위와 함께 저장
nums = [4, 1, 7, 3, 8, 5]
max_heap = []

for i in nums:
    heapq.heappush(max_heap, (-i, i))   # (우선순위, 값) 형태로 저장
print(max_heap)

print(heapq.heappop(max_heap)[1])   # 최댓값 pop
