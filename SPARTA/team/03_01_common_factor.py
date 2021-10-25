# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오
# 자연수 a, b < 10000
# 첫째 줄에는 최대공약수를, 둘째 줄에는 최소 공배수를 출력

# 공약수
# a = 12 [1, 2, 3, 4, 6, 12]
# b = 18 [1, 2, 3, 6, 9, 18]
# 최대공약수 : [1, 2, 3, 6] = 6
# n < 12
# 1 * x == 12

# 공배수
# a = [12, 24 ,36, 48, 60 ...]
# b = [18, 36, 54, 72 ...]
# 최소공배수 : 36

# 유클리드 호제법
# r = a%b
# (a,b) = (a,r)
input_a, input_b = input().split()
a = int(input_a)
b = int(input_b)

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            current_remainder = a % b
            a = current_remainder

        else:
            current_remainder = b % a
            b = current_remainder

    if a == 0:
        result = b
    else:
        result = a

    return result

# 최소 공배수 성질
# a = a1 * result
# b = b1 * result
# 최소공배수 = a1 * b1 * result
# 최소공배수 = a * b // result
result = a * b // gcd(a, b)


print(gcd(a, b))
print(result)
