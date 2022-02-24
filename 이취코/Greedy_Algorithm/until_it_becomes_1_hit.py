# 어떤 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고한다.
# 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
# 위 두 절차를 조합하여 N이 1이되는 최소한의 횟수를 구하여라

# 입력조건
# 첫째 줄에 N(2<= N <= 100,000)과 K(2 <= K <= 100,000)가 공백으로 구분되며 각각 자연수로 주어진다.
# 이때, 입력으로 주어지는 N은 항상 K보다 크거나 같다.

# 출력조건
# 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.

# 접근방식_연산 횟수 최적화 방법
# 1. N을 K로 나눴을 때, 나머지가 존재하는지 검사한다.
# 2. 존재한다면, 1번째 방법이 진행되야 할 횟수를 구한다. ((n // k) * k) -> 나머지가 존재하지 않는 타겟 값
# 3. 만약 n값이 k보다 작을 경우 반복문 탈출한다.
# 4. 그렇지 않다면, 2번 동작이 진행될 때마다, n값을 갱신하고 반복문을 반복한다.

n, k = map(int, input().split())
count = 0

while True:
    target = (n // k) * k
    count += (n - target)
    n = target

    if n < k:
        break

    count += 1
    n //= k

count += (n - 1)
print(count)