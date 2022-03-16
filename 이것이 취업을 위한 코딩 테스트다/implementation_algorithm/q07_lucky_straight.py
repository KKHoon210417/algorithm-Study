# 럭키 스트레이트

# 럭키스트레이트를 위해서는 아래 조건을 만족해야합니다.
# 캐릭터의 점수 N을 자릴수 기준으로 반으로 나누어 왼쪽 부분의 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황입니다.
# 현재 점수 N이 주어졌을 때, 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지 알려주는 프로그램을 작성하시오.

# 입력 조건
# 1. 첫째 줄에 점수 N이 정수로 주어집니다. 단 점수 N의 자릿수는 항상 짝수 형태로만 주어집니다.

# 출력 조건
# 2. 첫째 줄에 럭키 스트레이트를 사용할 수 있다면 "LUCKY"를 사용할 수없다면 "READY"를 출력하세요.

# 접근 방법
# 1. 주어지는 n을 반으로 나눈 위치의 인덱스 값을 찾습니다.
# 2. 해당 인덱스를 이용해 왼쪽 정수에 대해 for문, 오른쪽 정수에 대해 for문을 돌려 각 정수의 합을 비교합니다.
# 3. 합이 동일하면 LUCKY를 출력 아니면, READY를 출력

# 접근방법
n = str(input())

index = len(n) // 2

left_sum = 0
right_sum = 0

for i in range(index):
    left_sum = left_sum + int(n[i])
    right_sum = right_sum + int(n[i + index])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")