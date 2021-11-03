# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은
# 수를 모두 출력하는 프로그램을 작성하시오.

N, X = map(int, input().split())
num = list(map(int, input().split()))

for i in range(N):
    if num[i] < X:
        print(num[i], end=" ") # end=" "에는 원래 \n 개행문자가 들어간다 개행문제 대신에 다른 문자를 넣을 수 있다.
