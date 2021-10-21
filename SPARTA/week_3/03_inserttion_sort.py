input = [4, 6, 2, 9, 1]

# 4
# 4 6
# 4 6 2 -> 4 2 6 -> 2 4 6
# 2 4 6 9
# 2 4 6 9 1 -> 2 4 6 1 9 -> 2 4 1 6 9 -> 2 1 4 6 9 -> 1 2 4 6 9




def insertion_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
            print(i - j)
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!