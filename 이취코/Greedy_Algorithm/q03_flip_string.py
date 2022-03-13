# Q03 문자열 뒤집기

# 0과 1로만 이루어진 문자열 S가 있습니다.
# 문자열 S의 모든 숫자를 갖게하려고한다.
# 행동은 모든 연속된 숫자를 뒤집을 수 있습니다.
# 최소한의 행동만으로 모든 숫자를 갖게 만드는 프로그램을 작성하시오.

# 입력 조건
# 1. 첫째 줄에 0과 1로만 이루어진 문자열 S가 주어집니다. S의 길이는 100만보다 작습니다.

# 출력 조건
# 1. 첫째 줄에 다솜이가 해야하는 행동의 최소 횟수를 출력합니다.

# 접근 방법
# 1. 11110001111처럼 문자열이 주어질 때, 연속되는 숫자가 몇개의 그룹인지 확인합니다.
# 2. 연속되는 숫자의 그룹이 숫자를 기준으로 뒤집습니다.
# 3. 뒤집은 행동의 횟수를 출력합니다.

# 풀이_내꺼
# n = str(input())
#
# count = 0
# prv = n[0]
# for i in range(1, len(n)):
#     if prv == n[i]:
#         prv = n[i]
#         continue
#     else:
#         prv = n[i]
#         count += 1
#
# print(count - 1)

# 풀이_답지
data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))