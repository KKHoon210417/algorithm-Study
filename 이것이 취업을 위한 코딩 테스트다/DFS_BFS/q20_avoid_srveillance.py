# Q20 감시 피하기

# N x N 크기의 복도가 있습니다.
# 각 선생님들은 상, 하, 좌, 우 4가지 방향으로 감시를 진행합니다. 이때, 선생님은 장애물로 가로막히기 전까지 4가지 방향으로 학생을 볼 수 있습니다.
# 위칫값은 (행, 열)로 나타냅 O로 표시합니다니다.
# # 선생님이 존재하면 T, 학생이 존재하면 S 장애물이 존재하면.
# 장애물 3개를 설치하여 학생들이 선생님의 감시로부터 모든 학생이 피할 수 있는지 프로그램을 작성하시오.

# 입력 조건
# 1. 첫째 줄에 자연수 N이 주어집니다.
# 2. 둘째 줄에 N개의 줄에 걸쳐서 복도의 정보가 주어집니다. 각 행에서는 N개의 원소가 주어지며, 공백으로 구분합니다. 해당 위치에 학생이 있다면
#   S, 선생이 있다면 T, 아무것도 존재하지 않는다면 X가 주어집니다.

# 출력 조건
# 1. 첫째 줄에 정확히 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지 여부를 출력합니다.
#   가능하다면 Yes, 불가능하다면 No를 출력하세요

# 접근 방식
# 1. 모든 장애물 경우의 수에 따른, DFS, BFS를 실시해서 감시를 피할 수 있는지 체크한다.

# 풀이
from itertools import combinations

n = int(input())
board = []
teacher = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teacher.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))


def watch(x, y, direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False


def process():
    for x, y in teacher:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False


find = False

for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'
    if not process():
        find = True
        break
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')
