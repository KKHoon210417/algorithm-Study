# 1로 만들기

# 정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지 이다.
# 1. X가 5로 나누어 떨어지면, 5로 나눈다.
# 2. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 3. X가 2로 나누어 떨어지면, 2로 나눈다.
# 4. X에서 1을 뺀다.
# 정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하세요.
# 예)
# X = 26 -> 1) 26 - 1, 2) 25 /5, 3) 5 / 5 3번

# 입력 조건
# 1. 첫째 줄에 정수 X가 주어진다.

# 출력 조건
# 1. 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

# 접근 방식
# 1. 결과 값이 1이 될때, 종료되는 반복문을 만든다.
# 2. 1 ~ 4번의 순서로 if문을 만든다.
# 3. 반복문이 실행될 때 마다, 카운트한다.
# 4. 내가 보기엔 그리디 문제로 볼 수 도 있지 않나...? 값이 큰 값부터 시도해나가는 -> 아니네
# 5. 수정1 - 1 - > 26으로 만들어 볼까?
# 6. 수정1 - 1 -> 5 -> 25 -> 26
# 7. 수정2 - 경우의 수 카운트가 기록되는 리스트를 만들고
# 8. 수정2 - 리스트에 저장된 숫자 중 가장 작은 수를 출력해볼까

# 이해한 내용
# 1. DP 문제는 대게 작은 문제부터 생각하여, 규칙을 찾아 풀 수 있다.
# 2. 해당 문제에서는 5,3,2,-1의 방법을 이용해서 최소한의 동작으로 값을 구해야 한다.
# 3. 이를 위해서 각 x값에 따른 최소 값을 테이블에 저장해 놔야 할 필요성을 느낀다.
# 4. d[0] = 0, d[1] = 0, d[1] = 1, d[2] = 1, d[3] = 1, d[4] = 2, d[5] = 1, d[6] = 2, d[7] = 3, d[8] = 3
# 5. 위의 최소 값을 나열한 것 중 d[6]을 보면, 6에서 -1을 빼는 방법과 2로 나누는 방법 3으로 나누는 방법 3가지의 방법이 존재한다.
# 6. 이때, -1로 뺏다면, 5가 되고, 5일때(d[5])의 최솟값은 1이여서 2라는 횟수가 나온다.
# 7. 이때, 2로 나눴다면, 3이 되고, 3일때(d[3])의 최솟값은 1이여서 2라는 횟수가 나온다.
# 8. 이때, 3으로 나눴다면, 2가 되고, 2일때(d[2])의 최솟값은 1이여서 2라는 횟수가 나온다.
# 9. d라는 테이블에 이미 이전 계산했던 최솟값이 존재하기 때문에, 이를 이용해 각 조건에 맞게 동작을 취하고 해당 조합에서 나올 수 있는 최소
#   값을 d[x]에 넣어주면 된다,
# 10. 이렇게 작성한 d[x]는 이후 나올 정수에서 최솟값을 구하는데 도움이 된다.

# 풀이
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001

# 다이나믹 프로그래밍 진행(보텀업)
for i in range(2, x + 1):
    # -1을 했을 때, d[i]에 들어갈 최솟값은 이전 원소의 +1만큼이다.
    d[i] = d[i - 1] + 1
    # 2으로 나눴을 때, d[i]에 들어갈 최솟값은 d[i/2]에 +1을 한 값과 (d[i-1]+1) 중 작은 값이 최솟값이 된다.
    if i % 2 == 0:
        d[i] = min(d[i // 2] + 1, d[i])
    # 3으로 나눴을 때, d[i]에 들어갈 최솟값은 d[i/3]에 +1을 한 값과 (d[i-1]+1) 또는 2로 나눴을 경우 중 작은 값이 최솟값이 된다.
    if i % 3 == 0:
        d[i] = min(d[i // 3] + 1, d[i])
    # 5로 나눴을 때, d[i]에 들어갈 최솟 값은 d[i/5]에 +1을 한 값과 (d[i-1]+1) 또는 2로 나눴을 경우 또는 3으로 나눴을 경우 중 작은 값이 최솟 값이 된다.
    if i % 5 == 0:
        d[i] = min(d[i // 5] + 1, d[i])

print(d[x])