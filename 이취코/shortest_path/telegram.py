# 전보

# N개의 도시가 존재한다.
# 각 도시는 일방향 통신 라인이 존재한다면, 통신을 보낼 수 있다.
# 예 ) X -> Y와 같이 통신 라인이 존재한다면, X에서 Y로 보낼 수 있지만, Y에서 X로는 보낼 수 없다.
# 통신을 보낼때는, 각 통신 라인마다 일정 시간이 소요된다.
# C 도시에 위급 상황이 발생해서, 최대한 많은 도시에 메세지를 보내야한다.
# C지점에서 모든 지역에 메세지를 보낼때, 메세지를 보낼 수 있는 지역의 개수와 모든 메세지가 도달하는 시간을 구하는 프로그램을 작성하시오.

# 입력 조건
# 1. 첫째 줄에 도시의 개수 n, 통로의 개수 m, 메세지를 보내고자하는 도시 c가 주어진다.
# 2. 둘째 줄부터 M + 1번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다.(출발 도시, 도착 도시, 소요시간)

# 출력 조건
# 1. 첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력한다.

# 접근 방법
# 1. 한 지점에서 다른 모든 지점에 대한 최소 거리를 구해야 하기 때문에 다익스트라 알고리즘을 사용한다.
# 2. 입력되는 노드의 개수와 간선의 개수가 많은 관계로 eloge의 시간 복잡도가 소요되는 우선 순위 큐를 이용한 다익스트라를 쓴다.
# 3. C도시를 제외한 이동이 가능한 도시의 개수를 출력한다.
# 4. 모든 도시에 메시지가 도착한 시간을 출력해야 하므로 이동 거리가 가장 긴 노드의 길이를 출력한다.

# 풀이
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수, 시작 위치 입력
n, m, start = map(int, input().split())

# 간선의 개수를 저장할 그래프 초기화
graph = [[] for i in range(n + 1)]

# 최단 거리 리스트를 무한대로 초기화
distance = [INF] * (n + 1)

# 간선에 대한 정보를 graph에 저장한다.
for i in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y, z))

# 익스트라 알고리즘 구현
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 실행
dijkstra(start)

# 도달할 수 있는 지역의 개수
count = 0

# 도달할 수 있는 지역중, 가장 멀리 있는 지역의 최단 거리
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)
