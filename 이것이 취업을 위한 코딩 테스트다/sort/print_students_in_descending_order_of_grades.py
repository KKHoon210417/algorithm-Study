# 성적이 낮은 순서로 학생 출력하기

# N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하세요.

# 입력 조건
# 1. 첫 번째 줄에 학생의 수 N이 입력된다.
# 2. 두 번째 줄부터 N + 1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
# 3. 문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.

# 출력 조건
# 1. 모든 학생의 이름을 성적이 낮은 순서대로 출력한다.
# 2. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.

# 접근 방식 _ 실패
# 1. 1 ~ 100까지 크기가 제한되고 중복된 데이터가 많이 나오는 만큼 계수 정렬을 선정해서 풀이한다.
# 2. 1 ~ 100 크기의 리스트에 이름을 순서대로 추가한다.(성적이 같을 경우 학생 이름의 순서는 자유롭게 출력)

# 접근 방식 _ 풀이
# 1. sorted key 매개변수로 정렬한다.

# 풀이
n = int(input())
score_array = []

for i in range(n):
    name, score = input().split()
    name = str(name)
    score = int(score)
    score_array.append((name, score))

# 키를 이용하여, 점수를 기준으로 정렬
sorted_name_array = sorted(score_array, key = lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in sorted_name_array:
    print(student[0], end=' ')