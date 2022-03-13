# Q10 자물쇠와 열쇠

# 자물쇠는 N X N 크기의 정사각 격자 형태이다.
# 열쇠는 M X M 크기의 정사각 격자 형태로 되어 있다.
# 열쇠를 회전, 이동 시켜서 자물쇠의 빈 칸을 가득 채우는 프로그램을 작성하시오.
# 이때, 열쇠의 돌기부분과 자물쇠의 돌기부분이 맞닿아서는 안됩니다.

# 제한사항
# 1. key는 M X M 크기 2차원 배열입니다.
# 2. key는 N X N 크기 2차원 배열입니다.
# 3. M은 항상 N 이하입니다.
# 4. key와 lock의 원소는 0 또는 1로 이루어져 있습니다. 0은 홈 부분, 1은 돌기 부분을 나타냅니다.

# 접근 방법_풀이
# 1. 코딩 테스트 채점 환경에서는 1초에 2000만에서 1억 정도의 연산을 처리할 수 있다. 그러므로, 최대 20 X 20 크기의 2차원 리스트에 있는
#   모든 원소를 확인하는 완전 탐색을 이용해서 열쇠를 이동시키거나 회전하는 경우의 수를 다 적용해보자.
# 2. 완전 탐색을 수월하게 하기 위해 자물쇠 리스트의 크기를 3배 이상으로 변경하여 계산하자.
# 3. 열쇠 배열을 왼쪽 위부터 시작해서 한 칸씩 이동하는 방식으로 차례대로 자물쇠의 모든 흠을 채울 수 있는지 확인하면 된다.
# 4. 만약 자물쇠 부분이 전부 1이 되면 True, 그렇지 않고, 0이 있거나 또는 어느 원소가 2가 되면 False를 반환한다.
# 5. 이때, 2차원 리스트를 90도 회전한 결과를 반환하는 함수를 만든다.

# 풀이_해설

# 2차원 리스트 90도 회전 _ 필기해두고 두고두고 써먹기!
def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])  # 열 길이 계산
    result = [[0] * n for _ in range(m)]  # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3  # 3배 크기이기 때문에, 3으로 나눈다.
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)  # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼어 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False