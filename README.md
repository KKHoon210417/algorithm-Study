# algorithm-Study
Python 기반의 알고리즘 공부 Repository입니다.

## Card
<div>
  <img align='center' src="http://mazassumnida.wtf/api/v2/generate_badge?boj=zozo1591">
</div>
<br>

## 알고리즘 이론
<details>
<summary>그리디</summary>
<div markdown="1">
  
  - 그리디란, 현재 상황에서 지금 당장 좋은 것만 고르는 방식을 갖는 알고리즘이다.<br>
  주로 거스름돈 문제가 대표적인 문제이며 특징으로는 큰 단위가 작은 단위의 배수 형태일 때 그리디가 성립된다는 것이다.
  
    <details>
    <summary>예시</summary>
    <div markdown="2">
    
        <문제>
        도와주는 점원이다. 카운트에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
        손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

        <접근 방식>
        1. '10원 짜리로만 모두 거슬러 주도록 코드를 작성하면 최적의 해를 구할 수 있을까?'
        2. '큰 단위부터 거슬러준다면, 최적의 해를 구할 수 있지 않을까?'
        3. '그렇다면, 큰 수가 작은 수의 배수 형태를 갖추고 있나?'

        <풀이>
        n = 1260
        count = 0

        # 큰 단위의 화폐부터 차례로 확인
        coin_types = [500, 100, 50, 10]

        for coin in coin_types:
          count += n // coin # 해당 화폐로 거슬러줄 수 있는 동전의 개수 세기
          n %= coin # 거슬러 주고 남은 화폐 갱신

        print(count)
        
    </div>
    </details>
  
</div>
</details>



## 현재 진도
### BAEKJOON
- 단계별 알고리즘 풀이
  - 입출력과사칙연산
  - while문
  - if문
  - for문
  - 1차원배열 (진행중)

### Sparta
- 1~4주차 알고리즘(완료)


