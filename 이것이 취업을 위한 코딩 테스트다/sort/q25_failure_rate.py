# Q25 실패율

# 실패율을 다음과 같이 정의할 때, 실패율을 구하시오.
#   - 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터
# 내림차순으로 스테이지의 번호가 담겨 있는 배열을 return 하도록 solution 함수를 완성하세요.

# 접근 방법
# 1. n + 1의 길이를 갖는 리스트를 만들고 해당 리스트에 클리어한 사람의 스테이지를 넣습니다.
# 2. 해당 리스트를 이용해 스테이지 번호와 실패율을 튜플로 리스트에 저장합니다.
# 3. 실패율을 기준을 내림차순으로 스테이지 번호를 출력합니다.

# 풀이
N = 5
stages = [2, 1, 6, 2, 4, 3, 3]

def solution(N, stages):
    result = []
    success_stages = [0] * (N + 1)
    for stage in stages:
        if stage > N:
            for i in range(1, N):
                success_stages[i] += 1
        else:
            for i in range(1, stage + 1):
                success_stages[i] += 1
        

    for i in range(1, N + 1):
        if success_stages[i] == 0:
            failure_rate = 0
        else:
            failure_rate = stages.count(i) / success_stages[i]
        
        result.append((failure_rate, i))

    result.sort(key=lambda x: (-(x[0])))

    result_value = []
    for i in result:
        result_value.append(i[1])

    return result_value


print(solution(N, stages))