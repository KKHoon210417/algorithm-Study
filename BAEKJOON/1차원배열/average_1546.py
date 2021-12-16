N = int(input())

result = 0
array = list(map(int, input().split()))
max_value = max(array)
for i in array:
    new_score = i/max_value*100
    result += new_score

print(result/N)