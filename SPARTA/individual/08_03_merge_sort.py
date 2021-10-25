array = [5, 3, 2, 1, 6, 8, 7, 4]

# 병합정렬 : 정렬되어 있는 상태가 될때까지 쪼개서(배열내 요소가 한개 있을 때를 의미) 다시 합치면서 정렬하는 방식
#           Big_O(NlogN)
#           재귀함수를 사용한다.

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    return merge(left_array, right_array)


def merge(array1, array2):
    sorted_list = []
    array1_pointer = 0
    array2_pointer = 0
    while array1_pointer < len(array1) and array2_pointer < len(array2):
        if array1[array1_pointer] < array2[array2_pointer]:
            sorted_list.append(array1[array1_pointer])
            array1_pointer += 1
        else:
            sorted_list.append(array2[array2_pointer])
            array2_pointer += 1
    if array1_pointer >= len(array1):
        while array2_pointer < len(array2):
            sorted_list.append(array2[array2_pointer])
            array2_pointer += 1
    if array2_pointer >= len(array2):
        while array1_pointer < len(array1):
            sorted_list.append(array1[array1_pointer])
            array1_pointer += 1
    return sorted_list

print(merge_sort(array))