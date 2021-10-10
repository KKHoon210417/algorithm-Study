A = int(input())
B = int(input())


three = A*(B%10)
four = A*((B%100)-(B%10))
fours = four // 10
five = A*((B%1000)-(B%100))
fives = five // 100
six = five+four+three

print(three)
print(fours)
print(fives)
print(six)