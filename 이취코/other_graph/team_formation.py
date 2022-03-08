# 팀 결성

# 학교에서 학생들에게 0번부터 N번까지의 번호를 부여했다.
# 처음에는 모든 학생이 서로 다른 팀으로 구분되어 총 N + 1개의 팀이 존재했다.
# 선생은 합치기와 찾기 연산을 수행할 수 있다.
#   1. 합치기 연산은 두 팀을 합치는 연산이다.
#   2. 찾기 연산은 특정한 두 학생이 같은 팀에 속하는지 확인하는 연산이다.
# 선생이 M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인' 연산에 대한 연산 결과를 출력하는 프로그램을 작성하시오.

# 입력 조건
# 1. 첫째 줄에 N, M이 주어진다. M은 입력으로 주어지는 연산의 개수이다.
# 2. 다음 M개의 줄에는 각각의 연산이 주어진다.
# 3. 팀 합치기 연산은 0 a b 형태로 주어진다. 이는 a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다는 의미이다.
# 4. 같은 팀 여부 확인 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에 속해있는지를 확인하는 연산이다.
# 5. a와 b는 N이하의 양의 정수이다.

# 출력 조건
# 1. 같은 팀 여부 확인 연산에 대하여 한 줄에 하나씩 YES 혹은 No로 결과를 출력한다.

# 접근 방법
# 1. union, find 연산을 사용하는 것으로 봐 서로소 집합 알고리즘을 적용하면 될 것 같다.

# 풀이
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 팀의 개수와 합치기 연산의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 팀합치기 연산과 한팀 찾기 연산을 각각 수행
for i in range(e):
    w, a, b = map(int, input().split())
    if w == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end=" ")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

# 부모 테이블 내용 출력
print("부모 테이블: ", end=" ")
for i in range(1, v + 1):
    print(parent[i], end=" ")
