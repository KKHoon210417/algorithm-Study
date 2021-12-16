result = 1
for i in range(3):
    temp_val = int(input())
    result *= temp_val

array = []
for i in str(result):
    array.append(i)

for i in range(10):
    print(array.count(str(i)))