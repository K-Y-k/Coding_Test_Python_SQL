# Coding_Test_Practice_Python
내가 풀어본 코딩테스트 파이썬 소스코드 및 알고리즘 공부 (2022.07~)


# :page_facing_up: 목차
- <a href="#0"> 문제를 풀 때의 자세 </a>
- <a href="#0.5"> 코딩 실력 늘리기 팁 </a>
- <a href="#1"> 구현 </a>
- <a href="#2"> 스택, 큐, 덱 </a>
- <a href="#3"> 수학 </a>
- <a href="#4"> 그리디 알고리즘 </a>
- <a href="#5"> DP </a>
- <a href="#6"> 그래프 </a>
- <a href="#7"> 트리 </a>
- <a href="#8"> 이분 탐색 </a>
- <a href="#9"> 분할 정복 </a>
- <a href="#10"> 완전 탐색(브루트포스) </a>


## <b id="0"> 문제를 풀 때의 자세 </b>
- 각 문제의 맞는 순서대로 도식화로 표현하는 손 코딩을 해보고 그 순서대로 코딩해 본다.
- 코딩 먼저 하면 처음부터 다시 만들어야 할 수도 있기에 비효율적이다.
- 디버깅을 각 로직에서의 출력 형태로 나타내서 어디가 문제인지 확인하자.


## <b id="0.5"> 코딩 실력 늘리기 팁 </b>
- 30분~1시간은 충분히 생각해 보고 그 시간이 지체되면 풀이를 확인하기
- 풀이를 확인했다면 풀이의 코드 한 줄, 한 줄 모두 완벽히 이해하고 넘어가야 한다.
- 풀이를 봤거나 봐도 이해가 안 된 문제는 다시 풀어보는 리스트에 추가하고 나중에 다시 풀면서 풀이를 보지 않고 내가 손 코딩이 가능할 때까지 반복 
- 알고리즘 각 유형을 돌려가며 풀지 않고 같은 유형을 연속으로 풀면서 어떤 패턴인지 익숙해지기


## <b id="1"> 구현 </b>
- 문자열 처리, 자료구조, 수학 등이 관련된 문제가 나온다.
- 문자열 처리 관련해서는 split(), 딕셔너리, set, 슬라이스, count, index, replace, islower/isupper/isdiigit/isspace 등 활용해서 문자열 처리를 구현하는 위주의 문제가 나온다.
- 즉, 관련 함수들을 생각해서 활용하기


## <b id="2"> 스택, 큐, 덱 </b>
- 리스트에 넣고 빼고를 활용해야 하는 문제

- ### 스택
  * 한쪽 끝에서만 자료를 넣고 뺄 수 있는 자료구조
  * 자료를 넣는 것 = append(push)
  * 자료를 빼는 것 = pop
  * 제일 위(top)에 무엇이 있는지만 알 수 있는 자료 구조
  
  * #### 스택의 활용 문제 
    - ex1) 단어 뒤집기
      - 문장이 주어졌을 때 단어를 모두 뒤집는 문제 (12345순으로 넣으면 54321순으로 뒤집어서 나오기에)

    - ex2) 괄호 문제
      - 괄호 짝 조건) 
        - ① 닫는 괄호의 앞에 여는 괄호가 있어야 함
        - ② 다른 여는 괄호와 짝을 이루지 않아야 함
        - ③ 가장 가까운 여는 괄호가 짝
      
      여는 괄호 '('는 스택에 넣고 닫는 괄호 ')'일 시 최근에 넣은 '('를 지운다.
      
      이렇게 끝까지 확인하고 스택이 비어있으면 모두 짝을 이룬 것 남아있으면 짝 없음
      
      ')'가 왔는데 '('가 스택에 없으면 '('부족으로 짝 없음

  * push와 pop 시간 복잡도 = O(1)이므로 스택의 시간 복잡도 = O(N)

- ### 큐
  * 한쪽 끝에서만 자료를 넣고 다른 한쪽 끝에서만 뺄 수 있는 구조
  * 즉, 넣은 순서대로 나옴
  * BFS 알고리즘에서 주로 사용
  * 파이썬은 리스트가 아닌 collection.deque 사용

- ### 덱
  * 양 끝에서만 자료를 넣고 양 끝에서 뺄 수 있는 자료구조
  * 즉, stack과 queue의 기능 모두 이용할 수 있다.

## <b id="3"> 수학 </b>
- 사칙 연산, 진법, 최대공약수/최소공배수, 소수(에라토스테네스의 체), 팩토리얼 등의 문제
- 진법은 진법 관련 함수 생각해서 적용하자.
- 최대공약수 구하는 함수(gcd 함수 또는 유클리드 호제)를 생각해서 적용하자.


## <b id="4"> 그리디 알고리즘 </b>
1. 구하는 연산 공식을 정확히 집어야 한다.
2. 각 케이스에 맞는 조건식으로 정확히 집어야 한다.
- 탐욕적인 알고리즘으로 효율을 추구하는 것이 아닌 현재 상황에서 당장 좋은 것만 고르는 방법
- '가장 큰 순서대로', '가장 작은 순서대로'와 같은 기준을 제시한다. 즉, 주로 순서가 주어지고 연산을 적용하여 최대/최소 값을 구하는 문제
- 문자열, 정렬, 리스트, 반복문 등 기초적인 문법 활용 


## <b id="5"> DP </b>
- 작은 문제에서부터 큰 문제로 풀어가는 방식 
- 동일한 계산을 반복해야 할 때, 
  이전에 계산한 값을 메모리에 저장함으로써 동일한 계산의 반복 수행을 제거하여 프로그램 실행 속도를 빠르게 하는 기술
  
- DP라고 생각하기 기준
  1. 연속 관련 내용의 문제 
  2. 각 경우의 수의 최대/최소 값의 문제
  3. 경우의 수의 규칙을 구하는 문제
  4. 범위가 한정적으로 작게 주어진다.

- 풀이 방식
  * ① dp 배열 전체 초기화(2차원 배열도 고려) :  1차원 ex) -> d = [0] * (MAX+1)  / 2차원 ex) -> d = [[0]*N for _ in rangeM+1)]
  * ② 일정 패턴이 오기 전까지 초반 부분의 답을 초기화해두기 
  * ③ 작은 것으로 나누는 기준을 명확히 집어서 일정 규칙에 맞게 점화식을 세워 적용


## <b id="6"> 그래프 </b>
- 어떤 상황이 주어지면 
  1. 그래프로 모델링 한후 
  2. 알고리즘(ex) DFS/BFS/트리)을 적용해서 푼다.
- 즉, 그래프로 만드는 것이 제일 중요하다.

- ### 그래프 용어
  * 그래프: 정점과 간선(정점과 정점의 연결)으로 이루어진다.
  * 경로  : 정점 A에서 정점 B로 가는 경로
  * 사이클: 정점의 시작점과 도착점이 같은 경로
  * 단순 경로/단순 사이클: 같은 정점을 2번 이상 방문하지 않는 경로/사이클 (즉, 일반적인 경로/사이클이 이 뜻임)
  * 루프: 간선의 양 끝점(정점)이 같은 경우 ex) A->A
  * 가중치: 간선에 쓰여있는 값 
            즉 이는 이동거리/시간/비용 등을 표현한다.
            간선에 가중치 표기가 없으면 기본값은 1
  * 차수 : 해당 정점과 연결되어 있는 간선의 개수
    - In-degree: 해당 정점으로 들어오는 방향의 간선 개수
    - Out-degree: 해당 정점이 아닌 상대 정점으로 들어가는 방향의 간선 개수
          
- ### 그래프 방향
  - 그래프는 방향이 있는 그래프와 없는 그래프(=양방향)가 있다. 
     방향 없는 그래프는 모두 방향이 있게 만들어야 한다.
  - 정점A -> 정점B의 간선이 여러 개일 수 있다. 
    이때는 그때 문제 상황에 따라 처리해 주어야 한다.

- ### 그래프로 표현하기
  * 주로 사용하는 방식은 인접 리스트로 저장 방식
  * 리스트를 이용해서 구현한다.
  * A[i] = i와 연결된 정점을 리스트로 포함하고 있음

- ### 그래프 탐색
  * 목적: 임의의 정점에서 시작해서 연결되어 있는 모든 정점을 1번씩 방문하는 것
  * DFS
    - 하나의 정점에서 한 정점까지 끝까지 방문한 후 다시 돌아와서 다른 정점으로 가는 깊이 우선 탐색
    - 스택으로 구현, check[i]을 활용해서 방문하면 0에서 1로 변경, 재귀 호출로 구현 가능
    - 인접 리스트로 구현한 DFS의 시간 복잡도 = O(V+E) = O(E)
    - 이를 활용하는 예시) 사이클을 찾는 문제
  * BFS
    - 같은 너비이면 한 번에 가는 너비 우선 탐색
    - 큐로 구현
    - 최단거리를 구할 때는 DFS는 안되고 이 방식을 사용해야 한다.
    - 이를 활용하는 예시) 주변 이동하면서 구하는 문제

- ### 그래프 연결 요소 개수
  * ex1) 연결된 그래프가 나누어져 있으면 연결 요소 2개
  * ex2) 연결된 그래프가 하나만 있으면 연결 요소 1개
  * 즉, DFS/BFS의 시작 지점의 개수로 연결 요소의 개수를 구할 수 있다. (시작 지점을 새로 한다는 것은 다른 연결요소가 있다는 뜻이므로)

- ### 이분 그래프
  * 하나의 그래프를 2개로 나눌 수 있는 그래프
  * 이분 그래프의 구현은 DFS/BFS 모두 구현 가능


## <b id="7"> 트리 </b>
- ### 트리의 정의
  * 트리는 그래프이지만, 사이클이 없는 연결 그래프이기에 특징이 정점의 개수는 V개 간선의 개수는 V-1개이다.
  * 하지만 무조건 V개, V-1개라고 트리는 아니다. (왜냐하면 분리되어 있는 경우도 있기에 즉, 트리일 때의 성질) 
  * 즉, 모두 연결되어있다라는 조건이 추가되어야 한다.
  
- ### 트리의 조건
  * ① 정점의 개수=V, 간선의 개수=V-1
  * ② 모두 연결된 그래프 

- ### 트리의 루트
  * 트리는 루트가 정의되어 있지 않지만 내가 임의로 정의할 수 있다.
  * 트리의 제일 중요한 점으로 트리는 루트가 있을 수 있고 없을 수 있다!
  * 부모, 자식 관계
    - 루트가 있는 트리는 루트부터 아래로 방향을 정할 수 있고 이는 부모-자식 관계가 생긴다.
    - 부모가 없는 노드 = 루트 
    - 자식이 없는 노드(마지막 깊이의 노드들) = 단말 정점
  * 조상, 자손 관계
    - 조상은 자기 자신, 부모, 부모의 부모를 포함한다.
    - 자손은 자기 자신, 자식, 자식의 자식

- ### 트리의 종류
  #### 1. 이진 트리
    - 트리 중 가장 유명한 트리
    - 자식을 최대 2개만 가지는 트리
    
  #### 2. 포화 이진 트리
    - 단말 정점의 높이가 모두 같고 꽉 차있는 트리
    - 즉, 높이 h인 트리 노드 개수 = 2^h - 1

  #### 3. 완전 이진 트리
    - 포화 이진 트리에서 마지막 깊이에서 오른쪽 단말 노드에 일부가 없는 것
    - 즉, 왼쪽 단말 노드에 일부가 없는데 오른쪽 단말 노드에 일부가 있으면 완전 이진 트리가 아니다.
    - 하지만 포화 이진 트리처럼 꽉 차 있는 것도 완전 이진 트리에 포함된다.

- ### 트리의 표현
  * 트리는 그래프이므로 그래프에 저장하던 방식을 그대로 사용한다.
  * 루트가 있는 트리일 경우 = 트리의 부모만 저장하는 방식(=UnionFind 방식) : 
    
    모든 노드는 부모를 하나만 가지고 있고 부모가 없는 노드는 루트 하나만 있으므로 이 방식이 가능한 것
    
    -> 이 방식은 부모 찾는 시간은 빠르지만 자식 찾는 시간은 O(N)으로 느리다.
    
  * 완전 이진 트리인 경우 = 배열로 표현(=Heap, Segment Tree 방식)
    
    ex) 부모 노드가 x인 경우, 자식 노드는 2x, 2x+1로 나타낸다.

  * 이진 트리인 경우 = 구현체, 클래스를 정의해서 표현 가능

- ### 트리 순회(탐색)
  * 트리는 그래프이므로 DFS/BFS 모두 가능
  * DFS는 3가지 출력 순서가 있다. 노드 방문을 언제 할지의 차이
    - 프리오더(루트-왼쪽-오른쪽)   : 자식의 값을 구할 때 부모의 값을 이용해야 한다면 이 방식을 사용
    - 인오더(왼쪽-루트-오른쪽)     : BST에서 삭제를 구현할 때 사용(즉, 쓸 일 별로 없다), 이진 트리는 이 방식 사용 못함
    - 포스트오더(왼쪽-오른쪽-루트) : 거의 가장 많이 쓰고 중요함(자식의 정보를 이용해서 현재 노드의 값을 계산할 때 사용하므로)
                                   현재 노드의 값을 구할 때 자식의 값을 이용해야 한다면 이 방식을 사용
                 
- ### 트리 탐색
  * 트리는 그래프이므로 DFS/BFS 모두 가능
  * 트리는 사이클이 없으므로 임의 두 정점 사이의 경로는 1개이다.
  * 즉, 최단 거리를 구하는 문제이면 DFS/BFS로 구할 수 있다. 
  * 경로가 1개라서 찾은 그 경로가 최단 거리
                                  
- ### 트리의 지름
  * 트리에 존재하는 모든 경로 중 가장 긴 것이다.
  * 트리의 지름은 탐색 2번으로 구할 수 있다.
    - ① 한 정점 s에서 모든 정점까지의 거리를 구한다.(=DFS/BFS로 구함) 이때 가장 먼 거리인 정점을 u라고 하고
    - ② u에서 모든 정점까지의 거리를 구한다. 이때 가장 먼 거리인 정점을 v를 구한다.
    - ③ u와 v사이의 거리가 트리의 지름이다.
  * 포스트 오더를 이용해서도 구할 수 있다.


## <b id="8"> 이분 탐색 </b>
- 이진 탐색이란 데이터가 정렬돼 있는 배열에서 특정한 값을 찾아내는 알고리즘
- 이진 탐색은 주로 반복문 방식 / 재귀 함수 방식이 있다.
- 이분 탐색은 기준을 절반인 중간값으로 하면서 
  
  절반보다 작으면 좌측 데이터(끝의 값을 중간값-1로 조정), 
  
  절반보다 크면 우측 데이터(시작값을 중간값+1로 조정)로 범위를 줄여가며 탐색하는 과정으로 
  
  일반 배열을 모두 일일이 탐색하는 for 루프 보다 훨씬 빠르다.
- 만약 이분 탐색도 시간 초과가 발생하면 딕셔너리를 활용하자.


## <b id="9"> 분할 정복 </b>
- 문제를 즉각 해결할 수 있을 때까지 재귀적으로 둘 이상의 하위 문제(Sub-problem)들로 나누고(Divide) 
  문제를 해결한 다음 그 결과를 이용해 다시 전체 문제를 해결하며 합치는 방법
  
- 해결되는 문제들의 예시
  * ① 정렬 문제(퀵 정렬, 병합 정렬)
  * ② 큰 숫자 곱하기(Karatsuba 알고리즘) : n자릿 수 2개를 곱하여 결과를 나타내는 알고리즘
  * ③ 이진 탐색
  * ④ Closest Pair of Points 문제 : 모든 point의 쌍의 거리 중 최소의 거리를 찾는 문제
  * ⑤ Strassens's 알고리즘         : 두 행렬을 곱하는 효과적인 알고리즘
  * ⑥ Cooley-Tukey Fast Fourier Transform(FFT) 알고리즘 : 가장 일반적인 FFT 알고리즘

- 핵심 진행방식
  * ① 분할 : 동일한 타입의 하위 문제로 큰 문제를 분할한다.
             전체 데이터를 반으로 지속적으로 분할한다. 직접 문제가 해결되는 수준까지(1개 남을 때까지)
  * ② 정복 : 재귀적으로 하위 문제들을 해결한다.
             데이터 1개가 남으면 그 자체로 이미 정렬된 상태이다. 분할된 2개의 데이터를 정렬한다.(하위 문제 해결)
  * ③ 병합 : 적절히 해결된 결과를 사용해 큰 문제를 해결한다.
             정렬된 하위 문제를 병합하여 전체 내역을 정렬한다.

- 분할 정복과 DP는 문제를 잘 개 쪼개서 가장 작은 단위로 분할한다는 공통점이 있다.
- DP는 부분 문제가 중복되고 상위 문제 해결 시 재활용할 수 있는 메모이제이션 기법을 사용하지만
- 분할 정복은 부분 문제 중복이 없고 메모이제이션 기법을 사용하지 않는다는 차이점


## <b id="10"> 완전 탐색(브루트포스) </b>
- 가능한 모든 경우의 수를 다 체크해서 정답을 찾는 방법이다.
- 문제에서 주어지는 경우(방법)의 수가 1억 가지보다 작으면 이 방식으로 접근해도 좋을 수도 있다.
- 경우의 수가 많으면 그 경우의 수를 모두 적용해 봐야 하기에 불가하다.
   즉, 효율적으로 동작해야 하는 경우 이 방법이 사용되는데 제한이 따른다.
- 시간 복잡드 = O(방법의 수 * 방법 1개를 시도하는데 걸리는 시간 복잡도)
- 수행 순서
  * ① 문제의 가능한 경우의 수를 계산한다. (직접 계산을 통해 구해본다. 이 경우 대부분 손으로 계산 가능하다.)
  * ② 가능한 모든 방법을 다 만들어본다.
  * ③ 각 방법을 이용해 답을 구해본다.

- 수행 순서 2번의 모든 방법에는 다음과 같은 방법들이 있다.
  * ① Brute Force 기법   : 반복 / 조건문을 활용해 모두 테스트하는 방법
  * ② 순열(Permutation)  : 임의의 수열일 경우 n개의 원소 중 r개의 원소를 중복 허용 없이 나열하는 방법
  * ③ 재귀 호출
  * ④ 비트마스크         : 2진수 표현 기법을 활용하는 방법
  * ⑤ BFS, DFS를 활용

- 재귀/순열/비트마스크 중 재귀가 제일 중요하다.(순열/비트마스크를 재귀로 만들 수 있기에)
- 재귀 브루트포스 문제 방식은 1.순서의 문제 2.선택의 문제

- 백트래킹이란
  * 브루트포스는 모든 경우의 수를 조회하지만,
    
    재귀 함수를 이용해 브루트 포스를 하다 보면 더 이상 함수 호출이 진행되는 중에 의미가 없는 경우
   
    함수 호출을 중단하여 의미 없는 경우를 제외면서 브루트포스를 진행할 때를 의미한다. 
