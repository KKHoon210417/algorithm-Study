input = [4, 6, 2, 9, 1]

# 4 6 2 9 1

# 4
# 4 6
# 4 6 2 -> 4 2 6 -> 2 4 6
# 2 4 6 9
# 2 4 6 9 1 -> 2 4 6 1 9 -> 2 4 1 6 9 -> 2 1 4 6 9 -> 1 2 4 6 9

# for i in range(1, 5):
#     print()
#     for j in (range(i)):
#         print(i - j)

# 삽입 정렬 : 배열중 첫번재를 정렬되어 있는 상태라 가정하고 하나씩 뒤에서부터 비교해가면서 정렬해나간다.
# 핵심 정렬 : 첫번재는 정렬되어 있다 가정하기 때문에 0번째에서 정렬을 하지 않는다. (range(1, 5))
#            인덱스 값이 뒤인 값을 역순차적으로 비교하기 때문에 i - j 인덱스 값을 이용한다.

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in (range(i)):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return

insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!