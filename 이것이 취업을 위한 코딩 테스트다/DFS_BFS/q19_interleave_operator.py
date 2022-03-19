# Q19 연산자 끼워 넣기

# N개의 수로 이루어진 수열 A1, A2 ... An이 있습니다.
# 수와 수 사이에 끼워넣을 수 있는 N - 1개의 연산자가 주어집니다.
#   연산자는 +, -,*, / 로 이루어져 있습니다.
# 수와 수사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있는데 이때 주어진 수의 순서를 바꾸면 안됩니다.
# 나눗셈의 경우 몫만 취합니다.
# 음수를 나눌 경우 양수로 바꾼 뒤 몫을 취하고 다시 음수로 변환해줍니다.
# 만든 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 구하시오.

# 입력 조건
# 1. 첫째 줄에 수의 개수 N이 주어집니다.
# 2. 둘째 줄에는 A1 ~ An이 주어집니다.
# 3. 셋째 줄에는 합이 N - 1인 4개의 정수가 주어지는데, 차례대로 덧셈의 개수, 뺄셈의 개수, 곱셈의 개수, 나눗셈의 개수입니다.

# 출력 조건
# 1. 첫째 줄에 만들 수 있는 식의 결과의 최댓값을 출력합니다.
# 2. 둘째 줄에는 최솟값을 출력합니다.
# 3. 최댓값과 최솟값이 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어집니다. 또한 앞에서부터 계산했을 때,
#   중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고 10억보다 작거나 같습니다.

# 접근 방법
# 1. 완전탐색을 사용해보자, N개 만큼의 수열에 대해 각 자릿수에 최솟값 최대값을 입력합니다.
# 2. 점화식은 최솟값일 때, d[i] = min(d[n-1] + An, d[n-1] - An, d[n-1] * An, d[n-1] // An)
# 3. 점화식은 최대값 때, d[i] = max(d[n-1] + An, d[n-1] - An, d[n-1] * An, d[n-1] // An)

# 풀이
# n = int(input())
# a = list(map(int, input().split()))
# operator = list(map(int, input().split()))
#
# max_value = [0] * (n + 1)
# min_value = [0] * (n + 1)
#
# for i in range(1, n + 1):
#     max_value[i] = -1e9
#     min_value[i] = +1e9
#
# for index in range(1, n + 1):
#     if operator[0] > 0:
#         if (max_value[index - 1] + a[index]) > max_value[index]:
#             max_value[n] = max((max_value[index - 1] + a[index]), max_value[index])
#             operator[0] -= 1
#         if (min_value[index - 1] + a[index]) < min_value[index]:
#             min_value[n] = min((min_value[index - 1] + a[index]), min_value[index])
#             operator[0] -= 1
#     if operator[1] > 0:
#         if (max_value[index - 1] - a[index]) > max_value[index]:
#             max_value[n] = max((max_value[index - 1] - a[index]), max_value[index])
#             operator[1] -= 1
#         if (min_value[index - 1] - a[index]) < min_value[index]:
#             min_value[n] = min((min_value[index - 1] - a[index]), min_value[index])
#             operator[1] -= 1
#     if operator[2] > 0:
#         if (max_value[index - 1] * a[index]) > max_value[index]:
#             max_value[n] = max((max_value[index - 1] * a[index]), max_value[index])
#             operator[2] -= 1
#         if (min_value[index - 1] * a[index]) < min_value[index]:
#             min_value[n] = min((min_value[index - 1] * a[index]), min_value[index])
#             operator[2] -= 1
#     if operator[3] > 0:
#         if (max_value[index // 1] + a[index]) > max_value[index]:
#             max_value[n] = max((max_value[index - 1] // a[index]), max_value[index])
#             operator[3] -= 1
#         if (min_value[index - 1] // a[index]) < min_value[index]:
#             min_value[n] = min((min_value[index - 1] // a[index]), min_value[index])
#             operator[3] -= 1
#
# print(max_value)
# print(min_value)

# 풀이_해설
n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산의 수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색(DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            sub += 1
        if div > 0:
            div -= 1
            dfs(i + 1, now // data[i])
            sub += 1

dfs(1, data[0])

print(max_value)
print(min_value)