# 문제
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
# 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

# 예시 1)
# [2, 4, 5, 4, 6], M = 8, K = 3
# 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46

# 예시 2)
# [3, 4, 3, 4, 3], M = 7, K = 2
# 4 + 4 + 4 + 4 + 4 + 4 + 4 = 28

# 입력 조건
# 1. 첫째 줄에 N(2<=N<=1,000), M(1<=M<=10,000), K(1<=K<=10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 2. 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
# 3. 입력으로 주어지는 K는 항상 M보다 작거나 같다.

# 출력 조건
# 1. 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

# 접근 방식
# 1. M의 크기가 100억 이상처럼 커진다면, 시간 초과 판정을 받을 것이다.
# 2. 무식하게 일일이 더하는 과정을 없애고 수학적으로 접근하자.
# 3. [6, 6, 6, 5]와 같이 K + 1의 수열이 반복되는 형태를 갖는다.
# 4. int(M / (K + 1)) * K + M % (K + 1) 식을 이용해서 큰 값이 더해지는 횟수를 구한다.
# 5. M - 큰 값이 더해지는 횟수 를 이용해서 작은 값을 더해지는 횟수를 구한다.
# 6. 위 식을 각자 곱하고 더해 결과 값을 구한다.

# 풀이
# N, M, K 공백으로 구분하여 입력받기
N, M, K = list(map(int, input().split()))
# N개의 수를 공백으로 구분하여 입력받기
value_array = list(map(int, input().split()))

# value_array 정렬
value_array.sort()
first = value_array[-1]
second = value_array[-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(M / (K + 1)) * K
count += M % (K + 1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (M - count) * second  # 두 번째로 큰 수 더하기

print(result)