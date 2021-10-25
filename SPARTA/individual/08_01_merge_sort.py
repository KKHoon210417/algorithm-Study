array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

# 병합
def merge(array1, array2):
    sorted_list = []
    array_a_pointer = 0
    array_b_pointer = 0

    while array_a_pointer < len(array1) and array_b_pointer < len(array2):
        if array1[array_a_pointer] < array2[array_b_pointer]:
            sorted_list.append(array1[array_a_pointer])
            array_a_pointer += 1
        else:
            sorted_list.append(array2[array_b_pointer])
            array_b_pointer += 1
    if array_a_pointer == len(array1):
        while array_b_pointer < len(array2):
            sorted_list.append(array2[array_b_pointer])
            array_b_pointer += 1
    if array_b_pointer == len(array2):
        while array_a_pointer < len(array1):
            sorted_list.append(array2[array_a_pointer])
            array_a_pointer += 1
    return sorted_list


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!