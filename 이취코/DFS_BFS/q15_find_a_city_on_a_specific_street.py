# Q15 특정 거리의 도시 찾기

# 1 ~ N번까지의 도시와 M개의 단방향 도로가 존재한다.
# 모든 도로의 거리는 1이다.
# 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 출력하는 프로그램을 작성하시오.

# 입력 조건
# 1. 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어집니다.
# 2. 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 주어지며, 각 자연수는 공백으로 구분합니다.
#   이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미입니다.
#   단, A와 B는 서로 다른 자연수입니다.

# 출력 조건
# 1. X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력합니다.
# 2. 이때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력합니다.

# 접근 방법
# 1. 출발 노드 X로부터 최단 거리가 K인 모든 노드를 찾아야 하기 때문에, Queue를 사용해 BFS를 구현한다.
# 2. 최단 거리(노드의 Level)을 구해야하기 때문에 Level이 변경되는 시점을 기준으로 리스트를 만든다.
# 3. 그리고 리스트의 각 인덱스는 인덱스에 동일한 거리를 갖는 도시의 번호가 저장된다.

# 접근 방법_풀이
# 1. 도로의 거리가 동일한 조건 덕분에 너비 우선 탐색을 이용하여 해결하자
# 2. 방문 리스트 대신, 방문할 노드에 현재 노드 레벨 + 1을 할 수 있는 리스트를 선언하자
# 3. 최단 거리가 K인 도시가 있는지 없는지 확인하는 로직을 작성한다.


# 풀이
from collections import deque

n, m, k, x = map(int, input().split())

# 노드 간선 정보를 저장할 2차원 graph를 초기화
graph = [[] for i in range(n + 1)]
# 찾아야 할 최단 거리 변수
find_distance = k
# 시작 노드 변수
start = x

# 간선 정보 2차원 리스트에 입력받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 방문 정보와 거리가 저장되는 1차원 리스트 초기화
distance = [-1] * (n + 1)
# 시작 노드 방문 처리
distance[start] = 0

# BFS 함수 선언
def bfs(graph, start, distance):
    # 큐 라이브러리 사용
    q = deque([start])
    # 큐가 빌 때까지, 반복
    while q:
        # q에서 원소 하나 꺼내기
        now = q.popleft()
        # 노드(원소)와 연결된 모든 간선에 대해 반복 실행
        for i in graph[now]:
            # 방문하지 않은 노드는 방문처리하고, 큐에 추가
            if distance[i] == -1:
                distance[i] = distance[now] + 1
                q.append(i)

bfs(graph, start, distance)

for i in range(1, n + 1):
    if max(distance) < k:
        print(-1)
        break
    else:
        if distance[i] == k:
            print(i)

print(distance)

# # 최단 거리가 존재하는지 확인하는 로직_풀이
# # 최단 거리가 K인 모든 도시의 번호 오름차 순으로 출력
# check = False
# for i in range(1, n + 1):
#     if distance[i] == k:
#         check = True
#         print(i)
#
# # 만약 최단 거리가 K인 도시가 없다면, -1 출력
# if check == False:
#     print(-1)