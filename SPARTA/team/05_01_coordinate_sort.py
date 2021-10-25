def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    return merge(left_array, right_array)


def merge(array1, array2):
    sorted_list = []
    a_pointer = 0
    b_pointer = 0

    while a_pointer < len(array1) and b_pointer < len(array2):
        if array1[a_pointer][1] < array2[b_pointer][1]:
            sorted_list.append(array1[a_pointer])
            a_pointer += 1
        elif array1[a_pointer][1] > array2[b_pointer][1]:
            sorted_list.append(array2[b_pointer])
            b_pointer += 1
        else:
            if array1[a_pointer][0] < array2[b_pointer][0]:
                sorted_list.append(array1[a_pointer])
                a_pointer += 1
            else:
                sorted_list.append(array2[b_pointer])
                b_pointer += 1

    if a_pointer >= len(array1):
        while b_pointer < len(array2):
            sorted_list.append(array2[b_pointer])
            b_pointer += 1

    if b_pointer >= len(array2):
        while a_pointer < len(array1):
            sorted_list.append(array1[a_pointer])
            a_pointer += 1
    return sorted_list



N = int(input())


temp_list = []
for index in range(N):
    x, y = input().split()
    input_coordinate = [int(x), int(y)]
    temp_list.append(input_coordinate)

result = merge_sort(temp_list)
for i in result:
    print(i[0], i[1])

