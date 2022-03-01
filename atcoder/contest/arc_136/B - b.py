n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 인덱스 1, 2, 3인 경우 기본적으로
# 3, 2, 1
# 1, 3, 2
# 2, 1, 3 세가지 중 하나 연속으로 나올 수 없음
# 하지만, 동일한 원소가 있는 경우 고려해야
