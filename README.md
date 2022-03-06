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
      

<details>
<summary>DFS/BFS</summary>
<div markdown="2">
  
  
</div>
</details>
     
      
<details>
<summary>정렬</summary>
<div markdown="3">
  
  - 선택정렬
    
    가장 작은 것을 선택해서 앞으로 보내는 과정을 반복하는 정렬
    
    ```python
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    
    for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    	for j in range(i + 1, len(array)):
    		if array[min_index] > array[j]:
    			min_index = j
    		array[i], array[min_index] = array[min_index], array[i] # 스와프
    
    print(array)
    ```
    
    선택정렬의 시간복잡도는 O($N^2$)이다.
    
    그렇기에 선택정렬은 퀵 정렬과 기본 정렬 라이브러리에 비해 매우 비효율적이다.
    
    그래도, 특정한 리스트에서 작은 데이터를 찾는 일이 코딩 테스트에서 잦으므로 선택 정렬 소스코드 형태에 익숙해질 필요가 있다.
    
- 삽입정렬
    
    특정한 데이터를 적절한 위치에 삽입한다. 이때, 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정려되어 있다고 가정한다.
    
    이러한 이유로 삽입정렬의 맨 앞 데이터는 이미 정렬되어 있다고 가정되어 두번째 데이터부터 정렬이 시작된다.
    
    ```python
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    
    for i in range(1, len(array)):
    	for j in range(i, 0, -1):
    		if array[j] < array[j - 1]
    			array[j], array[j-1] = array[j-1], array[j]
    		else:
    			break
    
    print(array)
    ```
    
    삽입정렬의 선택정렬과 동일하게 시간 복잡도는 O($N^2$)이다.
    
    하지만, 리스트의 데이터가 거의 정렬되어 있다면, 매우 빠르게 동작한다.
    
    이럴 경우 퀵 정렬보다 빠르지만, 보통의 경우 퀵 정렬이 더 빠르다.
    
- 퀵 정렬
    
    기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
    
    퀵 정렬에서는 피벗(정렬을 위해 기준이 되는 값)이 사용된다. 이런 피벗을 설정하고 리스트를 분할하는 방식에 따라 퀵 정렬을 구분하는데, 여기서는 호어 분할 방식을 기준으로 설명한다.
    
    - 피벗은 리스트에서 첫 번째 데이터를 피벗으로 정한다.
    - 동작
        1. 리스트의 첫 번째 데이터를 피벗으로 설정하고, 리스트의 오른쪽에서부터는 피벗보다 작은 수를 찾는다, 리스트의 왼쪽에서는 피벗보다 큰 수를 찾는다.
            
            이렇게 찾은, 데이터의 자리를 서로 교체한다.
            
        2. 오른쪽과 왼쪽의 찾는 행위가 서로 엇갈리게 되면 작은 데이터와 피벗의 위치를 서로 변경한다.
        3. 피벗을 기준으로 분할된 파티션 각각을 재귀적으로 1번과 2번 동작을 반복한다.
        4. 현재 리스트의 데이터가 개수가 1개가 될 때, 정렬되었다고 정의하고 재귀를 빠져나온다.
    
    ```python
    # 일반적인 소스코드
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    
    def quick_sort(array, start, end):
    	if start >= end:
    		return
    	pivot = start # 피벗은 첫 번째 원소
    	left = start + 1
    	right = end
    	while left <= right:
    		# 피벗보다 큰 데이터를 찾을 때 까지 반복
    		while left < = end and array[left] <= array[pivot]:
    			left += 1
    		# 피벗보다 작은 데이터를 찾을 때까지 반복
    		while right > start and array[right] >= array[pivot]
    			right -= 1
    		if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
    			array[right], array[pivot] = array[pivot], array[right]
    		else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
    			array[left], array[right] = array[right], array[left]
    	# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    	quick_sort(array, start, right - 1)
    	quick_sort(array, right + 1, end)
    
    quick_sort(array, 0, len(array) - 1)
    print(array)
    ```
    
    ```python
    # 파이썬의 장점을 살린 퀵 정렬 소스코드
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    
    def quick_sort(array):
    	# 리스트가 하나 이하의 원소만을 담고 있다면 종료
    	if len(array) <= 1:
    		return array
    
    	pivot = array[0] # 피벗은 첫 번째 원소
    	tail = array[1:] # 피벗을 제외한 리스트
    
    	left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    	right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    	# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    	return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    
    print(quick_sort(array))
    ```
    
    퀵 정렬의 시간 복잡도는 O(NlogN)이다.
    
- 계수 정렬
    
    특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘이다.
    
    계수 정렬은 데이터의 ‘크기 범위가 제한되어 정수 형태로 표현할 수 있을 때’만 사용할 수 있다.
    
    ```python
    # 모든 원소의 값이 0보다 크거나 같다고 가정
    array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    
    # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
    count = [0] * (max(array) + 1)
    
    for i in range(len(array)):
    	count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
    
    for i in range(len(count)):
    	for j in rnage(count[i]):
    		print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
    ```
    
    계수 정렬의 시간복잡도는 O(N + K)이다.
    
    계수 정렬의 공간복잡도는 상당히 비효율적이다. 0과 999,999 단 두개만 존재해도, 0부터 100만개의 리스트의 크기를 갖는 리스트가 필요하기 때문이다. 이러한 이유로 ‘동일한 값을 가지는 데이터가 여러 개 등장할 때 적합하다’
    
    예) 학교 성적 정렬,
    
- 파이썬 정렬 라이브러리
    
    sorted는 정렬된 새로운 객체를 반환한다.
    
    sort는 해당 리스트를 정렬한다.
    
    key를활용하여 해당 key값을 기준으로 정렬할 수 있다.
    
    ```python
    # sorted
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    
    result = sorted(array)
    print(result)
    
    # sort
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    
    array.sort()
    print(array)
    
    # key 매개변수 사용
    array = [('바나나', 2),('사과', 5) ,('당근', 3)]
    
    def setting(data):
    	return data[1]
    
    result = sorted(array, key = setting)
    print(result)
    ```
    
    - **정렬 라이브러리로 풀 수 있는 문제** : 단순히 정렬 기법을 알고 있는지 물어보는 문제로 기본 정렬 라이브러리의 사용 방법을 숙지하고 있으면 어렵지 않게 풀 수 있다.
    - **정렬 알고리즘의 원리에 대해서 물어보는 문제** : 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리를 알고 있어야 문제를 풀 수 있다.
    - **더 빠른 정렬이 필요한 문제** : 퀵 정렬 기반의 정렬 기법으로 풀 수 없으며 계수 정렬 등의 다른 정렬 알고리즘을 이용하거나 문제에서 기존에 알려진 알고리즘의 구조적인 개선을 거쳐야 풀 수 있다.
  
</div>
</details>
      
      
<details>
<summary>이진 탐색</summary>
<div markdown="4">
  
  - 순차 탐색
    
    리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법.
    
    시간 복잡도 O(N)을 갖는다.
    
    ```python
    # 순차 탐색 소스코드
    
    def sequential_search(n, target, array):
        # 각 원소를 하나씩 확인하며
        for i in range(n):
            # 현재 원소가 찾고자 하는 원소와 동일한 경우
            if array[i] == target:
                return i + 1
    
    print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
    input_data = input().split()
    n = int(input_data[0]) # 입력할 원소 개수
    target = input_data[1] # 찾고자 하는 문자열
    
    print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합시다")
    array = input().split()
    
    # 결과
    print(sequential_search(n, target, array))
    ```
    
- 이진 탐색
    
    찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 방법.
    
    찾으려는 배열이 정렬되어 있어야 가능하다.
    
    - 이진 탐색(재귀함수)
    
    ```python
    # 이진 탐색 소스코드 구현(재귀함수)
    
    def binary_search(array, target, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        # 찾는 경우 중간점 인덱스 반환
    
        if array[mid] == target:
            return mid
    
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    
        elif array[mid] > target:
            return binary_search(array, target, start, mid - 1)
    
        elif array[mid] < target:
            return binary_search(array, target, mid + 1, end)
    
    # n과 target 입력
    n, target = list(map(int, input().split()))
    
    # 전체 원소 입력 받기
    array = list(map(int, input().split()))
    
    # 이진 탐색 수행 결과 출력
    result = binary_search(array, target, 0, n - 1)
    
    if result == None:
        print("원소가 존재하지 않습니다.")
    else:
        print(result + 1)
    ```
    
    - 이진 탐색(반목문)
    
    ```python
    # 이진 탐색 소스코드 구현(반복문)
    
    def binary_search(array, target, start, end):
        while start <= end:
            mid = (start + end) // 2
    
            # 찾은 경우 중간점 인덱스 반환
            if array[mid] == target:
                return mid
    
            # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
            elif array[mid] > target:
                end = mid - 1
            # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
            else:
                start = mid + 1
    
        return None
    
    # n과 target 입력
    n, target = list(map(int, input().split()))
    
    # 전체 원소 입력 받기
    array = list(map(int, input().split()))
    
    # 이진 탐색 수행 결과 출력
    result = binary_search(array, target, 0, n - 1)
    
    if result == None:
        print("원소가 존재하지 않습니다.")
    else:
        print(result + 1)
    ```
    
    - 팁
        - 1,000억 이상의 입력이 필요할 경우 input() 함수를 사용하면 동작 속도가 느려 시간초과로 오답 판정을 받을 수 있다.
            
            이럴 경우 sys 라이브러리를 사용하자.
            
            ```python
            import sys
            input_data = sys.stdin.readline().rstrip()
            
            print(input_data)
            ```
  
</div>
</details>
      

<details>
<summary>다이나믹 프로그래밍</summary>
<div markdown="5">
  
  다이나믹 프로그래밍으로 해결할 수 있는 대표적인 문제는 피보나치 수열이 있다.

피보나치 수열의 경우 i항을 구하기 위해 i - 1항과 i -2 항을 알아야되는데, i항을 구하기 위해 i - 1항과 i - 2항을 반복적으로 계산하는 것은 연산속도에 굉장한 제한을 줍니다.

이를 해결하기 위해 다이나믹 프로그래밍이 존재하는데, 동적인 메모리 공간을 만들어, 결과 값을 미리 저장해 놓고, 필요할 때, 사용하여 연산속도를 향상시키는 프로그래밍 기법입니다.

아래 대표적으로 피보나치 함수 소스코드를 보겠습니다.

```python
# 피보나치 함수 소스코드(재귀함수)

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))
```

이와 같이 코드를 구성한다면, 피보나치 수열은 구현이 가능하지만, x값이 100을 계산하려고 해도, 시스템 에러가 발생할 것입니다.

이런 문제를 해결하기 위한 다이나믹 프로그래밍 기법을 적용한 소스코드는 다음과 같습니다.

```python
# 피보나치 수열 소스코드(다이나믹 프로그래밍 적용)

# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료 조건(1 혹은 2일 때, 1을 반환)
    if x == 1 or x == 2:
        return 1

    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]

    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(3))
```

위 처럼 재귀함수를 이용해 다이나믹 프로그래밍 소스코드를 작성하는 방법을, 큰 문제를 해결하기 위해 작은 문제를 호출한다고 하여 **탑다운(Top-Down) 방식**이라고 말합니다.

```python
# 피보나치 수열 소스코드(반복적) 보텀업 방식

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
```

위 처럼 단순히 반복문을 이용하여 소스코드를 작성하는 경우 작은 문제부터 차근차근 답을 도출한다고 하여 **보텀없(Bottom-Up) 방식**이라고 말합니다.
  
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


