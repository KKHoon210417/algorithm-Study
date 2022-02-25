# 시각
# 정수 N이 입력되면, 00시 00분 00초부터 N시 59분 59초까지의 3이 나오는 모든 시각을 카운트하는 프로그램을 만드시오.

# 입력 조건
# 첫째 줄에 정수 N이 입력된다. (0 <= N <= 23)

# 출력 조건
# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.

# 접근 방법_답안 예시
# 1. if '3' in str(i) + str(j) + str(k)를 쓴다면, 3이 문자열 내에 3이 포함되어있는지 확인할 수 있다.

n = int(input())
count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1

print(count)