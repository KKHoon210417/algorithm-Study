# Q13 치킨 배달

# 크기가 N X N인 도시가 있습니다.
# 도시의 칸은 (r, c)와 같은 형태로 나타냅니다.
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리를 의미합니다.
# 각각의 집은 치킨 거리를 가지고 있습니다.
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합입니다.
# 임의의 두 칸(r1, c)와 (r2, c2)사이의 거리는 |r1 - r2| + |c1 - c2|입니다.
# 0은 빈칸 1은 집 2는 치킨집입니다.
# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 합니다. 어떻게 고르면
# 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하세요.

# 입력 조건
# 1. 첫째 줄에 N과 M이 주어집니다.
# 2. 둘째 줄부터 N개의 줄에는 도시의 정보가 주어집니다.
# 3. 도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈칸 1은 집 2는 치킨집을 의미합니다. 집의 개수는 2N개를 넘지 않으며,
#   적어도 1개는 존재합니다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같습니다.

# 출력 조건
# 1. 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력합니다.

# 접근 방법
# 1. for문을 이용해서, 2차원 리스트에 있는 치킨집과 집에대한 좌표 값을 갖는 각각의 리스트를 만듭니다.
# 2. 치킨집과 집에 대한 거리를 m번 계산할 때, 가장 작은 값을 구합니다....
# 3. how?

# 풀이 _ 해설
from itertools import combinations

n, m = map(int, input().split())
chichken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chichken.append((r, c))

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chichken, m))
print(candidates)

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidates):
    result = 0
    # 모든 집에 대해서
    for hx, hy in house:
        # 가장 가까운 치킨집을 찾기
        temp = 1e9
        for cx, cy in candidates:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)