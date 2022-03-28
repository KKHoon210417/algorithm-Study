# Q24 안테나

# 일직선상의 마을이 있다.
# 안테나를 설치하기로 결정했다. 이때, 안테나는 집이 있는 곳에만 설치할 수 있고, 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능합니다.
# 안테나를 설치했을 때 거리의 최솟 값을 출력하세요.
# N이 4일 때, 각 위치가 1, 5, 7, 9일 때를 가정하겠습니다.
# 이 경우 5의 위치에 설치했을 때, 안테나로부터 모든 집까지의 거리의 총합이 (4 + 0 + 2 + 4) = 10으로 최소가 됩니다.

# 접근 방법
# 1. 주어진 리스트를 정렬합니다.
# 2. 리스트의 가운데 값에 안테나를 설치합니다.
# 3. 해당 값이 최솟값입니다.

# 풀이
n = int(input())
home_array = list(map(int, input().split()))

home_array.sort()

min_value = 1e9
result_index = 0

for i in range(n):
    antenna = home_array[i]
    result = 0
    for j in home_array:
        result += abs(antenna - j)
    if min_value > result:
        result_index = antenna
        min_value = result

print(result_index)
print(min_value)