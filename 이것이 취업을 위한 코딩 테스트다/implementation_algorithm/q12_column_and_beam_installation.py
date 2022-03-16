# Q12 기둥과 보 설치

# 기둥과 보를 이용해서 구조물을 설치할 수 있습니다.
#   - 기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
#   - 보는 한쪽 끝부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 합니다.
# 단, 바닥은 벽면의 맨 아래 지면을 말합니다.
# n X n 크기의 정사각 격자 형태이며, 맨 처음 벽면은 비어 있습니다.


# 제한 사항
# [x, y, a, b] x, y는 좌표를 의미하고, a는 0일경우 기둥 1일 경우 보를 의미합니다. b는 0일 경우 삭제 1일 경우 설치를 의미합니다.
# 벽면을 벗어나게 기둥, 보를 설치할 수 없습니다.
# 바닥에 보를 설치하는 경우는 없습니다.
# 보는 오른쪽 방향으로 설치 & 제거, 기둥은 위쪽 방향으로 설치 & 제거합니다.
# 최종 구조물은 [x, y, a]의 형태를 갖습니다. x, y,는 기둥,보의 교차점 좌표입니다. a는 0이면 기둥 1이면 보를 나타냅니다.
# return값은 x의 값을 기준으로 오름차순을 합니다.


# 접근 방법
# 1. build_frame을 갖고 반복문을 돌립니다.
# 2. build_frame[0:2]는 좌표 변수에 넣고 build_frame[2:4]는 각각 보와 기둥인지 추가 삭제인지에 대한 변수에 넣습니다.
# 3. 보일 경우 좌표를 우측으로 한칸 증가시키는 방향으로 기둥일 경우 위로 한칸 증가시키는 방향으로 dx, dy를 설정합니다.
# 4. 만약 추가할 경우 result = []에 그 종류와 좌표를 저장합니다.


# 풀이_해설
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 설치된 것이 '기둥' 인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위' 라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False  # 아니라면 거짓반환
        elif stuff == 1:  # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기등 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False  # 아니라면 거짓반환
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:  # 삭제인 경우
            answer.remove([x, y, stuff])  # 일단 삭제를 해본 뒤에
            if not possible(answer):  # 가능한 구조물이 아니라면 다시 설치
                answer.append([x, y, stuff])
        if operate == 1:  # 추가인 경우
            answer.append([x, y, stuff])  # 일단 설치해본 뒤
            if not possible(answer):  # 가능한 구조물인지 확인
                answer.remove([x, y, stuff])  # 불가능할 경우 다시 삭제한다.
    return sorted(answer)  # x를 기준으로 정렬된 값을 출력
