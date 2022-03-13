# Q08 문자열 재정렬

# 알파벳 대문자와 숫자 0~9로 이뤄진 문자열입력이 주어진다.
# 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

# 입력 조건
# 1. 첫째 줄에 하나의 문자열 S가 주어진다.

# 출력 조건
# 1. 첫째 줄에 문제에서 요구하는 정답을 출력합니다.

# 접근 방법
# 1. 주어진 문자열로 반복문을 돌린다.
# 2. 문자가 주어질 경우 string 문자열에 저장한다.
# 3. 숫자가 주어질 경우 number에 값을 더합니다.
# 4. 최종적으로 문자열을 오름차 순으로 정렬시키고 number를 문자열로 변경하여 string에 합친다.

# 풀이
s = input()
number = 0
string = ''

for i in s:
    if not i.isalpha():
        number += int(i)
    else:
        string += i

sorted_string = ''.join(sorted(string))

result = sorted_string + str(number)
print(result)