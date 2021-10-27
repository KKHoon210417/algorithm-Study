K = int(input())

total_price = []    # 합계를 계산할 금액이 모여있는 리스트
for i in range(K):
    price = int(input())    # 재민이가 불러주는 값을 'price'라는 변수에 넣는다.
    if price == 0:          # 만일 'price'의 값이 0이라면 앞에 금액을 잘못 부른거기 때문에 .pop 메소드를 이용해서 이전 금액을 꺼낸다
        total_price.pop()
    else:                   # price가 0이 아니라면 total_price 변수에 금액을 넣는다.
        total_price.append(price)

print(sum(total_price))
