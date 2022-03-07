# 미래 도시

# 미래도시에는 1번부터 N번까지의 회사가 있고 서로 도로를 통해 연결되어 있다.
# 방문 판매원 A는 1번 회사에 있고, X번 회사에 방문해 물건을 판매하려고한다.
# 연결된 회사는 양방향으로 이동할 수 있고, 이동하는데 1만큼이 소비된다.
# 방문 판매원 A는 K번 회사에 소개팅이 있다.
# 방문 판매원은 1번회사에서 시작해 K번 회사를 방문한 뒤 X번 회사로 가는 것이 목표이다.
# 방문 판매원이 최소한의 시간으로 이동할 수 있는 프로그램을 작성하시오.

# 입력 조건
# 1. 첫째 줄에 전체 회사의 개수 n과 경로의 개수 m이 공백으로 구분되어 차례대로 주어진다.
# 2. 둘째 줄부터 m + 1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
# 3. m + 2번째 줄에는 x와 k가 공백으로 구분되어 차례대로 주어진다.

# 출력 조건
# 1. 첫째 줄에 방문 판매원 A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력한다.
# 2. 만약 X번 회사에 도달할 수 없다면 -1을 출력한다.

# 접근 방법
# 1. 1 -> K에 대한 최소한의 거리, K -> X에 대한 최소한의 거리 두가지에 대한 방문 거리가 필요하므로 플로이드 워셜을 사용한다.
# 2. 이때, 입력 노드의 개수가 100개 이하인 이유도 있다.(만일 없었다면, 다익스트라 알고리즘을 두번 쓰지 않았을까?)
# 3. 플로이드 워셜 알고리즘으로 구현된 2차 graph에서 [1][k]에 대한 값과 [k][x]값을 구해 서로 더한 값을 출력한다.
# 4. 만일, [1][k] 또는 [1][x] 둘 중 하나라도 갈 수 없다면, -1을 출력한다.

# 풀이
INF = int(1e9)

# 노드의 개수와 간선 개수 입력
n, m = map(int, input().split())
# 2차원 리스트를 만들고 모든 값 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 이동하는 값에 대해서, 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 초기 간선에 대한 값을 이용해 그래프 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# k와 x에 대한 위치를 저장한다.
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 실행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(n + 1):
    for b in range(n + 1):
        # 도달할 수 없는 경우, 무한이라고 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우, 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()


# 1 -> K + K -> X 에 대한 이동 결과를 더한 값을 출력한다.
if graph[1][k] == INF or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])