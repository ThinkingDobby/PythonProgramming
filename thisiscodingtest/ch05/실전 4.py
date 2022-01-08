n, m = map(int, input().split())
data = [list(map(int, input())) for i in range(n)]


def dfs(x, y, cnt, ans):
    if not (0 <= x < n and 0 <= y < m):
        return

    if x == n - 1 and y == m - 1:
        ans.append(cnt) # 최솟값 비교 위해 리스트에 추가(먼 길을 먼저 갈 수 있음)
        return

    if data[x][y] == 1:
        data[x][y] = 0
        dfs(x, y - 1, cnt + 1, ans)
        dfs(x, y + 1, cnt + 1, ans)
        dfs(x - 1, y, cnt + 1, ans)
        dfs(x + 1, y, cnt + 1, ans)
        data[x][y] = 1  # 재귀 풀리면서 원상복구 해야(먼 길을 먼저 갈  수 있음) -> 중복된 노드를 방문하는 경우 생김
        return


a = []
dfs(0, 0, 1, a)
print(min(a))

# 깊이 우선 탐색 시 먼길로 돌아서 갈 수도 있으며(이어져 있는 길로 먼저 이동하기 때문), 따라서 목적지까지 가는 모든 경우를 계산해야 최솟값을 알 수 있음(여러 경로 확인하기 위해 결과적으로 여러 번의 전체 탐색 수행됨)
# 너비 우선 탐색이 더 효율적: 가장 가까운 노드부터 탐색하기 때문에 최초 접근 시에만 변경 허용 시 -> 항상 가장 가까운 거리 기록됨(전체 탐색 한 번만 하는 것)