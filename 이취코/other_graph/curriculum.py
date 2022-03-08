# 커리큘럼_!!!!다시 해보기!!!!

# 동빈이는 N개의 강의를 듣고자 한다. 모든 강의는 1번부터 N번까지 번호를 갖는다.
# 또한, 동시에 여러 개의 강의를 들을 수 있다고 가정한다.
# 모든 강의에는 선후 관계를 갖는다.
# 예) N = 3일 때, 3번 강의의 선수 강의로 1번과 2번 강의가 있고 1번과 2번 강의는 선수 강의가 없다고 가정하자.
#   1번 강의 : 30시간, 2번 강의 : 20시간, 3번 강의 : 40시간
#   이 경우 1번 강의를 수강하기까지의 최소 시간은 30시간, 2번 강의를 수강하기까지는 최소 20시간, 3번 강의를 수강하기까지는 최소 70시간이다.
# 동빈이가 듣고자하는 N개의 강의 정보가 주어졌을때, N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력하는 프로그램을 작성하시오.

# 입력 조건
# 1. 첫째 줄에 동빈이가 듣고자 하는 강의의 수 N
# 2. 다음 N개의 줄에는 각 강의의 강의 시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호가 자연수로 주어지며, 각 자연수는
#   공백으로 구분한다. 이때, 강의 시간은 100,000 이하의 자연수이다.
# 3. 각 강의 번호는 1번부터 N까지로 구성되며, 각 줄은 -1로 끝난다.

# 출력 조건
# 1. N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한줄에 하나씩 출력한다.

# 접근 방법
# 1. 우선 방향성이 있는 과목들의 나열한 리스트를 구해야 하기 때문에, 위상 정렬을 사용합니다.
# 2. 이후, 각 노드들의 비용을 저장할 max_cost를 선언한다,
# 3. max_cost_array에 각 노드에 도달하기 위한 max_cost를 저장한다. or 출력한다.

# 풀이
from collections import deque

# 노드의 개수 입력받기
v = int(input())

#모든 노드에 대한 진입차수는 0으로초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 리스트 초기화
graph = [[] for i in range(v + 1)]
# 노드까지의 비용이 저장될 리스트 초기화
max_cost_array = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보 입력받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    max_cost_array[i] = data[0]
    for j in data[1:-1]:
        graph[j].append(i)
        # 진입 차수 1 증가
        indegree[j] += 1

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        temp_cost = 0
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 현재 노드까지 오기 위한 소요 시간을 저장한다.
            temp_cost = max(max_cost_array[i], max_cost_array[now] + max_cost_array[i])
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                max_cost_array[i] = temp_cost
                q.append(i)

    for i in max_cost_array[1:]:
        print(i)

topology_sort()