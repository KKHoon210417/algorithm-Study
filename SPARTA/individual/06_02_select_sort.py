input = [4, 6, 2, 9, 1]

# 배열중 가장 작은 요소를 맨 앞 의 요소와 교체한다.
# 핵심 정보 : for문이 돌때마다 비교하는 맨 앞 요소를 하나씩 증가 시켜줘야한다. tip : i + j
#           발견한 작은 요소와 맨 앞 요소의 위치를 변경 해야 한다. a, b = b, a
# big-O : n의 제곱
def selection_sort(array):
    n = len(array)
    for i in range(n-1):                            # 0
        min_index = i                               # 3
        for j in range(n-i-1):                      # 4
            if array[min_index] > array[i+j+1]:     # 4
                min_index = i + j + 1
        array[i], array[min_index] = array[min_index], array[i] # 교체를 단순이 자리잡아주는 것이 아니라 두개의 위치를 교체하는 것이 핵심!
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!