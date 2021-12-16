resultSet = set()
for i in range(10):
    n = int(input())
    result = n % 42
    resultSet.add(result)

print(len(resultSet))