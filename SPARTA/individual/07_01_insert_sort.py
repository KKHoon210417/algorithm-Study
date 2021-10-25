input = [4, 6, 2, 9, 1]

# 4 6 2 9 1

# 4
# 4 6
# 4 6 2 -> 4 2 6 -> 2 4 6
# 2 4 6 9
# 2 4 6 9 1 -> 2 4 6 1 9 -> 2 4 1 6 9 -> 2 1 4 6 9 -> 1 2 4 6 9

def insertion_sort(array):
    result = [4]
    n = len(array)
    for index in range(n):
        result.append(array[index])
        for i in range(len(result)-1):
            if result[len(result)-1-i] < result[len(result)-2-i]:
                result[len(result) - 1 - i], result[len(result)-2-i] = result[len(result)-2-i], result[len(result) - 1 - i]
            else:
                break
    print(result)
    return result


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!