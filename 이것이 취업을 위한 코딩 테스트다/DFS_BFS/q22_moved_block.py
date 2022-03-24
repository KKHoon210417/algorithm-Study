# Q22 블록 이동하기

# 2 x 1 크기의 로봇이 있다.
# N x N 크기의 맵이 존재하고, 최종적으로 로봇이 (N, N)위치에 어느 한 부위라도 존재하면 프로그램이 종료된다.
# (N, N)위치에 도착하는 최소 시간을 구하는 프로그래밍을 작성하시오.
# 조건은 아래와 같다.
#   1. N x N 크기의 맵에 1은 벽 0은 빈칸을 의미합니다.
#   2. 로봇은 앞 또는 뒤로 움직일 수 있습니다.
#   3. 로봇은 90도씩 회전할 수 있습니다. 단, 회전하는 위치에 벽이 존재해서는 안됩니다.(대각선상에)
#   4. 로봇이 회전할 때, 어느 위치든 축이 될 수 있습니다.
#   5. 맵의 좌측 상단은 (1,1)입니다. 로봇은 (1,1), (1,2)인 상태로 시작합니다.
#   6. 로봇이 회전하거나 이동할 때마다 1초가 경과됩니다.

# 제한 사항
# 1. board의 한 변의 길이는 5 이상 100 이하입니다.
# 2. board의 원소는 0 또는 1입니다.
# 3. 로봇이 처음에 놓여 있는 칸(1, 1) (1, 2)는 항상 0으로 주어집니다.
# 4. 로봇이 항상 목적지에 도착할 수 있는 경우만 입력으로 주어집니다.

# 접근 방법
# 1. 최소 시간을 구해야 하므로 BFS로 접근해보자.
# 2. 90도 회전에 대한 함수를 작성한다.
# 3. 로봇이 현재 위치에서 90도 회전할 수 있는지 확인하는 함수를 작성합니다.(매개변수로 방향과 위치)
# 4. 상하좌우로 움직이는 dx, dy를 작성합니다.

# 풀이
from collections import deque


def get_next_pos(pos, board):
    next_pos = []  # 이동 가능한 위치 반환
    pos = list(pos)  # 현재 위치 정보를 리스트로 변환
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + \
                                                             dy[i]
        # 이동하고자 하는 두 칸이 비어 있다면, 이동 가능한 위치 리스트에 저장
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos2_next_x), (pos1_next_y, pos2_next_y)})

    # 로봇이 가로로 놓여있을 때,
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 로봇이 세로로 놓여있을 때,
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    return next_pos


def solution(board):
    # 맵 외각을 벽으로 둘러싸는 형태로 변형
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0
