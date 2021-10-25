input = [4, 6, 2, 9, 1]
input1 = [2, 3, 8, 9, 10, 23, 78, 0, 23, 4, 78, 53, 4, 1]


def bubble_sort(array):
    for i in array:
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def bubble_sort1(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

bubble_sort1(input1)
print(input1)  # [1, 2, 4, 6, 9] 가 되어야 합니다!