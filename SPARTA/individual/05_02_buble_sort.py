input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        # i만큼 반복될 수록 뒤에서 뒤에서 i만큼은 이미 정렬이 되있기 때문에 계산할 필요가 없다.
        for j in range(5 - i -1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                print(j)
    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!