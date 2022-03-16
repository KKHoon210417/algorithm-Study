# 부품 찾기
# 부품 N개가 있다.
# 각 부품은 정수 형태의 고유한 번호가 있다.
# 이 중에 M개 종류의 부품을 찾아야한다.
# M개 종류의 부품이 모두 있는지 확인하는 프로그램을 작성하시오

# 입력 조건
# 1. 첫째 줄에 정수 N이 주어진다.
# 2. 둘째 줄은 공백으로 구분하고, n개의 정수가 주어진다.
# 3. 셋째 줄에는 정수 M이 주어진다.
# 4. 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다.

# 출력 조건
# 1. 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes, 없으면 no를 출력한다.

# 접근 방법
# 1. 모든 리스트를 오름차 순으로 정렬한다.
# 2. M의 리스트를 반복문을 돌려 이진탐색을 실행한다.

# 풀이
n = int(input())
n_array = list(map(int, input().split()))

m = int(input())
m_array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return print("no")

    mid = (start + end) // 2

    if array[mid] == target:
        return print("yes")

    elif array[mid] > target:
        binary_search(array, target, start, mid - 1)

    elif array[mid] < target:
        binary_search(array, target, mid + 1, end)

n_array.sort()

for i in m_array:
    binary_search(n_array, i, 0, n - 1)