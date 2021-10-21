# d(75) = 75 + 7 + 5 = 87
# 33 -> 33+3+3 = 39 -> 39 + 3 + 9 = 51 -> 51 + 5 + 1 =57 -> 57 + 5 + 7 = 69
# 33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141

# dn = n + n//
# n_list = list(map(int, str(n)))
# dn = n + n[0] + n[1] + n[2] ... n[len(n_list]
# self_number = dn으로 나오지 않는 값들을 의미한다.
def self_number():
    max_num = 10000
    n = 1
    dn_list = []
    while n <= max_num:
        n_list = list(map(int, str(n)))
        sum_n = n
        for n_num in n_list:
            sum_n += n_num

        dn_list.append(sum_n)
        n += 1

    self_number = list(set(list(range(1, max_num + 1)))-set(dn_list))
    self_number.sort()
    for i in self_number:
        print(i)
    return

self_number()