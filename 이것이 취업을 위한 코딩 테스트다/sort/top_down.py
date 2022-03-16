# 위에서 아래로

# 하나의 수열에는 다양한 수가 존재한다.
# 이러한 수는 크기에 상관 없이 나열되어 있다.
# 이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다.
# 수열을 내림차순으로 정렬하는 프로그램을 작성하시오.

# 입력 조건
# 1. 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다.(1 <= N <= 500)
# 2. 둘째 줄부터 N + 1 번째 줄까지 N개의 수가 입력된다. 수의 범위는 1 이상 100,000 이하의 자연수이다.

# 출력 조건
# 1. 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다. 동일한 수의 순서는 자유롭게 출력해도 괜찮다.

# 접근 방식1
# 1. sorted를 이용해 내림차 순으로 정렬한다.

# 접근 방식2
# 1. 퀵 정렬을 사용해 리스트를 정렬한다.

# 풀이1
# n = int(input())
#
# sequence_list = []
# for i in range(n):
#     sequence_list.append(int(input()))
#
# sorted_sequence_list = sorted(sequence_list, reverse=True)
#
# for i in sorted_sequence_list:
#     print(i, end=' ')

# 풀이2
n = int(input())

sequence_list = []
for i in range(n):
    sequence_list.append(int(input()))

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] >= array[pivot]:
            left += 1
        while right > start and array[right] <= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(sequence_list, 0, len(sequence_list) - 1)

for i in sequence_list:
    print(i, end=' ')