input = 20

# 피보나치 수열
# 1, 1, 2, 3, 5, 8, 13, 21 ...
# f(n) = f(n-1) + f(n-2)
def fibo_recursion(n):
    if n == 2 or n == 2:
        return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))  # 6765