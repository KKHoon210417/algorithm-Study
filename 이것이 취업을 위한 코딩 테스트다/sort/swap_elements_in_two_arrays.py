# 두 배열의 원소 교체

# 두 배열 A와 B가 있다.
# 두 배열은 N개의 원소로 구성되어 있으며, 원소는 모두 자연수이다.
# 최대 K번 바꿔치기 연산을 수행할 수 있다.
# 바꿔치기란 A와 B의 원소를 서로 바꾸는 것을 의미한다.
# 최대 K번 바꿔치기 연산을 수행해서 배열 A의 모든 원소의 합이 최댓값을 출력하는 프로그램을 작성하시오.

# 입력 조건
# 1. 첫 번째 줄에 N, K가 공백으로 구분되어 입력된다.
# 2. 두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다.
# 3. 세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다.

# 출력 조건
# 1. 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력한다.

# 접근 방법
# 1. A의 가장 작은 값과 B의 가장 큰 값을 서로 바꾼다.
# 2. 이때, A값이 B의 값보다 크면, 1번을 실행하지 않고, 배열 A의 모든 합을 출력한다.

# 풀이
n, k = map(int, input().split())

a_array = list(map(int, input().split()))
b_array = list(map(int, input().split()))

a_array.sort()
b_array.sort(reverse=True)

for i in range(k):
    if a_array[i] < b_array[i]:
        a_array[i], b_array[i] = b_array[i], a_array[i]
    else:
        break


print(sum(a_array))