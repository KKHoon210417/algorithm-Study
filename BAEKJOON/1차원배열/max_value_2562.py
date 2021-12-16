array = []
for i in range(9):
    temp_val = int(input())
    array.append(temp_val)

print(max(array))
print(array.index(max(array))+1)