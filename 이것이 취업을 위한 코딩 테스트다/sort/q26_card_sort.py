# Q26 카드 정렬하기

# 정렬된 두 묶음의 숫자 카드가 있을 때 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A + B번의 비교를 해야합니다.
# 매우 많은 숫자 카드 묶음이 존재할 때, 최소한의 카드 비교를 해야하는 최소 비교 횟수를 출력하는 프로그램을 작성하시오.
# 예) 10, 20, 40 -> 10 + 20 = 30 -> 30 + 40 = 70 -> 100
#   10, 20, 40 -> 10 + 40 = 50 -> 50 + 20 = 70 -> 120

# 접근 방법
# 1. 모든 카드 묶음을 오름차순으로 정렬합니다.
# 2. 해당 리스트를 순차적으로 더해줍니다.

# 풀이
# from collections import deque

# n = int(input())
# cards = []

# for i in range(n):
#     cards.append(int(input()))

# cards.sort(reverse=True)

# result = 0
# while cards:
#     card = cards.pop()
#     result 

# print(cards_value)
# print(result)

# 풀이_해설
import heapq

n = int(input())

# 힙에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

# 힙(heap)에 원소가 하나 남을 때 까지
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)