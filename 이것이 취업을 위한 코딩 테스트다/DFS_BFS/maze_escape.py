# 미로 탈출
# N x M 크기의 직사각형 형태의 미로에 갇혀있다.
# 동빈이의 위치는 (1, 1)이고, 미로의 출구는 (N, M)의 위치에 존재한다.
# 괴물이 있는 부분은 0, 괴물이 없는 부분은 1로 표시되어 있다.
# 미로는 반드시 탈출할 수 있는 형태로 제시된다.
# 이때, 미로를 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요.
# 칸을 셀때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

# 입력 조건
# 1. 첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어집니다.
# 2. 다음 N개의 줄에는 각각 M개의 정수(0과 혹은 1)로 미로의 정보가 주어집니다.
# 3. 각각의 수들은 공백 없이 붙어서 입력으로 제시됩니다.
# 4. 시작칸과 마지막 칸은 반드시 1이다.

# 출력 조건
# 1. 첫째 줄에 최소 이동 칸의 개수를 출력한다.

# 접근 방법
# 1. (0, 0) 좌표에서 DFS를 실시한다.
# 2. (N, M)을 방문하는 순간 반복문은 종료된다.

# 접근 방법 _ 풀이
# 1. BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문에 적합.
# 2. BFS로 인접한 노드를 방문할 때, 각 노드의 값을 1씩 증가시킨다.
# 3. 최종적으로 graph[n][m]의 노드의 값을 출력하면 최소 이동 노드 개수가 나온다.

# 풀이
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(x,y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0,0))