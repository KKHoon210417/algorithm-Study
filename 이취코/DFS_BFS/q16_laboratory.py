# Q16 연구소

# 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려한다.
# 연구소의 크기는 N X M인 직사각형으로 나타낼 수 있고, 직사각형은 1 X 1 크기의 정사각형으로 나누어져있습니다.
# 정사각형은 빈칸 또는, 벽입니다.
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있습니다.
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 합니다.
# 이때, 0은 빈칸, 1은 벽, 2는 바이러스가 있는 곳입니다.
# 벽을 세웠을 때, 만들어질 수 있는 안전 영역의 최댓값을 구하는 프로그램을 작성하시오.

# 입력 조건
# 1. 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어집니다.
# 2. 둘째 줄부터 N개의 줄에 지도의 모양이 주어집니다. 0은 빈칸, 1은 벽 2는 바이러스가 있는 위치입니다. 2의 개수는 2보다 크거나 같고,
#   10보다 작거나 같은 자연수입니다.
# 3. 빈칸의 개수는 3개 이상입니다.

# 출력 조건
# 1. 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력합니다.

# 접근 방법
# 1. 바이러스를 막을 수 있는 방법은 벽을 세우는 것이고, 바이러스가 퍼지는 것을 최대한 막아야 하니 바이러스의 가장 가까운 벽을 막는 것이 핵심!
# 2. 경로 탐색을 통해서, 바이러스가 존재하는 위치에서 발생할 수 있는 감염 블록을 전부 계산한다.
# 3. 이때, 2번에 대한 탐색하기 전, 삼중 for문을 이용해서 벽 3개를 설치하는 상황을 설정한다.
# 4. 그 중, 감염된 블록의 갯수가 가장 작은 경우의 수를 선정하고 (그래프의 크기 - 벽의 개수 - 감염된 블록의 갯수)로 안전 영역의 크기를 구한다.

# 접근 방법_풀이
# 1. 벽 3개를 세우는 경우의 수에 대해 연산을 진행해야한다.
# 2. 안전 영역의 크기를 구하는 것은 DFS 또는 BFS를 사용하여 계산한다.
# 실제 풀이방법____
# 3. 초기에 비어 있는 모든 공간 중에서 3개를 골라 벽을 설치한다.
# 4. 매번 벽을 설치할 대마다, 각 바이러스가 사방으로 퍼지는 것을 DFS/BFS로 계산하여 안전 영역을 구한다.


# 풀이_정답
n, m = map(int, input().split())
data = []   # 초기 맵 리스트
temp = [[0] * m for i in range(n)]  # 벽을 설치한 뒤의 맵 리스트

# 맵에 빈 공간, 벽, 바이러스에 대한 데이터 입력
for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)를 이용해 바이러스가 사방으로 퍼지도록 하기,
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)


# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                score += 1

    return score

# DFS를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)

# # 풀이_내가 시도해봄.
#
# n, m = map(int, input().split())
#
# graph = []
#
# # 2차원 리스트 입력받기
# for i in range(n):
#     graph.append(list(map(int, input().split())))
#
# def dfs(graph, x, y):
#     if x >= n or x < 0 or y >= m or y < 0:
#         return False
#     if graph[x][y] == 1:
#         return False
#     if graph[x][y] == 2:
#         graph[x][y] = graph[x][y] + 1
#     # 상하좌우에 대한 동작 성립
#     dfs(graph, x + 1, y)
#     dfs(graph, x - 1, y)
#     dfs(graph, x, y + 1)
#     dfs(graph, x, y - 1)
#
#
# dfs(graph, 0, 0)
#
# print(graph)