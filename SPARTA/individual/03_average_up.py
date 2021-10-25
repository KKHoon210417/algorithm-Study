# 첫째 줄에는 테스트 케이스 개수 C
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N이 첫 수로 주어지고,
# 이어서 N명의 점수가 주어진다. 점수는 0 보다 크거나 같고, 100보다 작거나 같은 정수
C = int(input())

for i in range(C):
    score_group = list(map(int, input().split()))
    avg = sum(score_group[1:])/score_group[0]
    cnt = 0
    for socre in score_group[1:]:
        if socre > avg:
            cnt += 1
    rate = cnt/score_group[0] * 100
    print(f'{rate:.3f}%')
