# 상하좌우
# 여행가 A가 존재한다고 할 때, N X N 크기의 정사각형 공간위에 서 있다.
# 이 공간은 1 X 1 크기의 정사각형으로 나눠져있다.
# 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N X N) 이다.
# 여행가 A는 주어지는 문자에 따라 (1, 1)에서 부터 시작해 이동을 한다.
# 주어지는 문자는 U(위로 1칸), D(아래로 1칸), L(왼쪽으로 1칸), R(오른쪽으로 1칸) 이다.
# 이때, 갈 수 없는 위치로 문자가 지시한다면, 해당 문자는 무시한다.
# 계획서가 주어졌을 때, 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.

# 입력 조건
# 첫재 줄에 공간의 크기를 나타내는 N이 주어진다.(1 <= N <= 100)
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1 <= 이동 횟수 <= 100)

# 출력 조건
# 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백으로 구분하여 출력한다.

# 접근 방식
# 1. 이동할 계획서를 리스트로 만들고 반복문 돌립니다.
# 2. 여행자 A의 위치가 x = 1, y = 1이라고 가정하고, 주어지는 문자 별로 x값과 y값을 변화시킨다.
#   U(y+=1), D(y-=1), L(x-=1), R(x+=1)
# 3. 이때, (1<= x, y <=N) 값을 벗어날 경우 해당 문자는 무시한다.
# 4. 반복문이 끝나고 나오는 x, y 값을 출력한다.

n = int(input())
plan_list = list(map(str, input().split()))
x, y = 1, 1

for plan in plan_list:
    if plan == "U" and x > n:
        x -= 1
    elif plan == "D" and x < n:
        x += 1
    elif plan == "L" and y > 1:
        y -= 1
    elif plan == "R" and y < n:
        y += 1

print(x, y)