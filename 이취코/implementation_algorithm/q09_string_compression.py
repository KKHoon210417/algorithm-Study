# Q09 문자열 압축

# 문자열 압축을 하고자 한다. 아래의 예를 확인하세요.
# 예) "aabbacc"의 경우 "2a2b3c"와 같이 표현할 수 있습니다.
#   이때, 문자열을 1개 이상 단위로 잘라서 압축할 수 도 있습니다.
#   abcabcdede의 경우 문자열 2개 단위로 자르면, abcabc2de로 나타낼 수 있습니다.
#                   문자열 3개 단위로 자르면, 2abcdede로 나타낼 수 있습니다.
# 압축할 문자열 s가 주어질 때, 위에 설명한 방법으로 1개 이상의 단위로 문자열을 잘라서 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return
#   하도록 solution을 완성해주세요.

# 제한사항
# 1. s의 길이는 1 이상 1000이하 입니다.
# 2. s는 알파벳 소문자로만 이루어져 있습니다.

# 접근 방법
# 1. 문자열의 단위를 하나씩 증가시키면서, 출력되는 결과값의 최대 값을 구한다.
# 2. 이때, 문자열의 단위는 주어진 문자열의 절반보다 클 수 없다.
# 3. 대체 "x / ababcdcd / ababcdcd 가 왜 안나눠진다는거지...?

# 풀이
s = "aabbaccc"

def solution(s):
    answer = len(s)
    # 문자열 단위를 하나씩 증가시키면서 결과 값 비교하기
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer

print(solution(s))