# baekjoon 1110
# n = 26
# 26
# 2+6=8 -> 68
# 6+8=14 -> 84
# 8+4=12 -> 42
# 4+2=6 -> 26
number = input()

def add_cycle(number):
    n = 0
    number_temp = number
    while True:
        if len(number_temp) == 1:
            number_temp = "0" + number_temp
        number_sum = str(int(number_temp[0]) + int(number_temp[1]))
        number_temp = number_temp[-1] + number_sum[-1]
        n += 1
        if number == number_temp:
            return print(n)

add_cycle((number))