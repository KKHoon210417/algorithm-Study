# 도시 분할 계획

# N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다.
# 마을의 이장은 마을을 2개의 분리된 마을로 분할할 계획을 세우고 있다.
# 각 마을은 집들은 서로 연결되도록 분할해야한다.
# 마을에는 집이 하나 이상 있어야 한다.
# 이때, 분할된 마을이 최소한의 유지비로 길이 유지될 수 있을 수 있는 최적의 프로그램을 작성하시오.

# 입력 조건
# 1. 첫째 줄에 집의 개수 N개, 길의 개수 M이 주어진다. N은 2이상 100.000 이하인 정수이고, M은 1 이상 1,000,000이하인 정수이다.
# 2. 그 다음 줄부터 M줄에 걸쳐 길의 정보가 A, B, C 3개의 정수로 공백으로 구분되어 주어지는데,
#   A번 집과 B번 집을 연결하는 길의 유지비가 C라는 뜻이다.

# 출력 조건
# 1. 첫째 줄에 길을 없애고 남은 유지비 합의 최솟값을 출력한다.

# 접근 방법
# 1. 크루스칼 알고리즘을 이용해 마을 하나에 대해서 신장 트리를 구현한 테이블을 구현합니다.
# 2. 그렇게 되면 현재 모든 집들은 서로 연결된 상태이기도 하며 사이클이 존재하지 않는 상태를 갖습니다.
# 2. 이때, 간선 하나를 제거하게 되면 마을이 두개로 나눠지게 되고 최소한의 비용을 위해 가장 높은 비용의 길을 테이블에서 제거한다.
# 3. 해당 테이블의 합이 유지비의 최솟값이다.

# 풀이
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때 까지, 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = []

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(v + 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소로 비용을 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합을 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result.append(cost)

# 가장 비용이 큰 값을 제거
result.pop()
# 결과 출력
print(sum(result))