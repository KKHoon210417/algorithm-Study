# Q18 괄호 변환

# 카카오에 신입 개발자로 인사한 "콘"은 선배 개발자로부터 개발역량 강화를 위해 다른 개발자가 작성한 소스코드를 분석하여 문제점을 발견하고
# 수정하라는 업무 과제를 받았습니다. 소스를 컴파일하여 로그를 보니 대부분 소스코드 내 작성된 괄호가 개수는 맞지만 짝이 맞지 않는 형태로 작성되어
# 오류가 나는 것을 알게 되었습니다.
# 수정해야할 소스 파일이 너무 많아서 고민하던 "콘"은 소스코드에 작성된 모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열을 알려주는
# 프로그램을 다음과 같이 개발하려고 합니다.



# 접근 방법
# 1. 문자열이 균형잡힌 괄호 문자열임을 판별하는데에 DFS를 사용합니다.

# 접근 방법_풀이
# 1. 재귀적으로 문제 해결해야한다.
# 2. 이 문제는 구현 문제이다.

# 풀이
# 균형 잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# 올바른 괄호 문자열인지 판단
def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # 올바른 괄호 문자열이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # 올바른 괄호 문자열이 아니라면 아래의 과정을 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer