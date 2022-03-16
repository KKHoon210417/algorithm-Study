# Q11 뱀

# N X N 크기의 정사각 보드가 존재하고, 그 위에는 사과가 놓여져 있다.
# 뱀은 좌측 상단에서 시작하고 뱀의 길이는 1입니다.
# 벽에 닿거나 또는 자기 몸에 닿으면 게임이 끝납니다.
# 조건
# 1. 먼저 뱀의 몸길이를 늘려 머리를 다음 칸에 위치시킵니다.
# 2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않습니다.
# 3. 만약 이동한 칸에 사과가 없다면, 몸 길이를 줄여서 꼬리가 위치한 칸을 비워줍니다.
#   즉, 몸 길이는 변화지 않습니다.
# 이 게임이 몇초에 끝나는지 계산하세요.

# 입력 조건
# 1. 첫째 줄에 보드의 크기 N이 주어집니다.
# 2. 둘째 줄에 사과의 개수 K가 주어집니다.
# 3. 다음 K개의 줄에 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열의 위치를 의미합니다.
# 4. 다음 줄에는 뱀의 방향 변환 횟수 L이 주어집니다.
# 5. 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며,
#   게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽 또는 오른쪽으로 90도 방향을 회전시킨다는 뜻입니다.
#   X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어집니다.

# 출력 조건
# 1. 첫째 줄에 게임이 몇 초에 끝나는지 출력합니다.

# 접근 방법
# 1. N X N 크기의 2차원 리스트를 만들고 사과가 존재하는 자리에 1을 설정합니다.
# 2. 방향 전환에 대한 함수를 만듭니다. direction(dir)
# 3. 뱀이 존재하는 위치를 2라고 설정을 합니다.
# 4. 방향 전환하는 입력을 리스트 튜플 형태로 만들고, 튜플의 0번 인덱스가 0이 되면, 방향 전환을 실시하고, 튜플을 제거합니다.
# 5. 매 동작마다, 시간 카운트를 1씩 증가시킵니다.
# 6. 매 동작마다, 이동할 수 있는지 확인하고 이동할 수 없는 경우 게임을 끝내고 시간 카운트를 출력합니다.

# 풀이
from collections import deque

n = int(input())

# n * n 크기의 2차원 리스트 초기화
graph = [[0] * n for i in range(n)]

# 맵에 사과 위치 세팅
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1

# 이동 명령어 튜플 & 리스트 형태로 저장
s = int(input())
move = deque([])
for i in range(s):
    m, d = input().split()
    m = int(m)
    move.append((m, d))

# 초기 바라보고 있는 방향(동쪽으로)
direction = 0

# 동, 남, 서, 북 방향 정의
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def change_direction(dir):
    global direction
    if dir == 'D':
        direction += 1
        if direction >= 4:
            direction = 0
    else:
        direction -= 1
        if direction <= -1:
            direction = 3


def solution(graph, move):
    global direction
    global n
    # 시작 지점 설정
    now_x = 0
    now_y = 0
    # 시간 카운트 변수 선언
    time_count = 0
    # 뱀의 몸 위치 구하기
    snake_length = deque([(0, 0)])

    now = move.popleft()
    move_count = now[0]
    move_dir = now[1]

    while True:
        if time_count == move_count:
            change_direction(move_dir)
            if move:
                now = move.popleft()
                move_count = now[0]
                move_dir = now[1]
        time_count += 1

        nx = dx[direction] + now_x
        ny = dy[direction] + now_y
        # 맵을 벗어난 경우 게임 시간을 출력하고 종료
        if nx < 0 or n <= nx or ny < 0 or n <= ny:
            return time_count
        # 자기 자신을 건드릴 경우 게임시간을 출력하고 종료
        if graph[nx][ny] == 2:
            return time_count
        # 그렇지 않을 경우, 사과가 있다면, 몸 길이 증가 없다면 몸만 이동
        if graph[nx][ny] == 1:
            snake_length.append((nx, ny))
            for i in snake_length:
                graph[i[0]][i[1]] = 2
            now_x = nx
            now_y = ny
        else:
            for i in snake_length:
                graph[i[0]][i[1]] = 0
            snake_length.popleft()
            snake_length.append((nx, ny))
            for i in snake_length:
                graph[i[0]][i[1]] = 2
            now_x = nx
            now_y = ny

print(solution(graph, move))


