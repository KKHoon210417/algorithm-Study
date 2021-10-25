# N킬로그램 배달 [3, 5] 봉지
# 18kg -> 5kg*3 3kg*1
N = int(input())

bag = 0
while N >= 0:
    if N % 5 == 0:
        bag += (N // 5)
        print(bag)
        break
    N -= 3
    bag += 1
else:
    print(-1)