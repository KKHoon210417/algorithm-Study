# Q21 인구 이동

# N x N 크기의 땅이 있습니다.
# 각각의 땅 (r, c)에는 나라가 존재합니다. 나라의 이름은 A[r][c]입니다.
# 인접한 나라 사이에는 국경선이 존재합니다.
# 인구이동이 진행되는데 다음의 조건에 따라 이동합니다.
#   - 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 엽니다.
#   - 위의 조건에 의해 열어야 하는 국경선이 모두 열렸다면, 인구 이동을 시작합니다.
#   - 국경선이 열려 있어 인접한 칸막을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 합니다.
#   - 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 됩니다. 편의상 소수점은 버립니다.
#   - 연합을 해체하고, 모든 국경선을 닫습니다.
# 각 나라의 인구수가 주어졌을 때, 인구 이동이 몇번 발생하는지 구하는 프로그램을 작성하세요.

# 입력 조건
# 1. 첫째 줄에 N, L, R이 주어집니다.
# 2. 둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어집니다. r행 c열에 주어지는 정수는 A[r][c]의 값입니다.
# 3. 인구 이동이 발생하는 횟수가 2000번보다 작거나 같은 입력만 주어집니다.

# 출력 조건
# 1. 인구 이동이 몇번 발생하는지 첫째 줄에 출력합니다.

# 접근 방법
# 0. 모든 동작은 while(L <= 각각의 모든 국가 <= R)가 될 때까지 무한히 반복합니다.
# 1. 국가 보드 national_board=[]을 초기화합니다.
# 2. L명 이상 R명 이하일 경우 national_board에 해당 국가를 표시합니다.
# 3. 각 국가를 확인하고, 인접한 나라(국경선이 안닫힌)의 인구수를 나라의 모든 인구수의 합에 연합나라의 수로 나눈 값을 넣습니다.
# 4. 3번 동작을 모든 칸(국경선이 닫힌 나라를 제외한)에서 실행합니다.
# 5. 이후, 인구이동을 +1 해주고 다시 while문을 확인합니다.

# 풀이
# n, l, r = map(int, input().split())
# board = []
# national_board = [[0] * n for i in range(n)]
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# for i in range(n):
#     board.append(list(map(int, input().split())))
#
# for i in range(n):
#     for j in range(n):
#         if board[i][j] <= r and board[i][j] >= l:
#             national_board[i][j] = 1
#
# def checked_borders(borders):
#     for i in borders:
#         for j in i:
#             if j == 0:
#                 return True
#     return False
#
# while checked_borders(national_board):
#     for i in range(n):
#         for j in range(n):
#             if national_board[i][j] == 1:
#                 continue
#             else:
#                 people = board[i][j]
#                 national_count = 1
#                 if n > i + 1 and 0 <= i + 1 and n > j and 0 <= j:
#                     if national_board[i+1][j] == 0:
#                         people += board[i+1][j]
#                         national_count += 1
#                 if n > i - 1 and 0 <= i - 1 and n > j and 0 <= j:
#                     if national_board[i-1][j] == 0:
#                         people += board[i-1][j]
#                         national_count += 1
#                 if n > i and 0 <= i and n > j + 1 and 0 <= j + 1:
#                     if national_board[i][j+1] == 0:
#                         people += board[i][j+1]
#                         national_count += 1
#                 if n > i and 0 <= i and n > j - 1 and 0 <= j - 1:
#                     if national_board[i][j-1] == 0:
#                         people += board[i][j-1]
#                         national_count += 1
#             national_people = people // national_count
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] <= r and board[i][j] >= l:
#                 national_board[i][j] = 1

# 해설_풀이
from collections import deque

n, l, r = map(int, input().split())

# 전체 나라의 정보를 입력받는다.
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def process(x, y, index):
    # x, y 위치와 연결된 나라 정보를 담는 리스트
    united = []
    united.append((x, y))

    # 너비 우선 탐색을 위한 큐 자료구조정의
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복(BFS)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하기
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1

print(total_count)