# AI-Programming
AI Programming 수업 (with Colab)

<br><br>
------
### 💜 Local Search 
#### 1. HillClimbing Algorithm
   - 최고점이나 최저점을 찾는 방법

#### 2. First choice 알고리즘 => TSP => 시각화
+ 길찾기 알고리즘
+ 랜덤으로 뽑아서 최적점 찾기
+ 내가 설정한 구간 내 최적점을 찾아줌  (구간 내 전역)
+ 시간이 오래 걸림 

#### 3. Steepest => ★경사하강법★ => 수식 => 시각화(matplot.lib)
+ 특정 방정식(수식)에서만 사용
+ 시간이 빠름 (앞의 값에서 빼면서 계산)
+ 최적점을 못찾을 수도 있음



---
+ TSP
   1. 정점 => 인접행렬
   2. 계산방법 결정 => 맨하탄, 유클리드
      + 인접행렬과 같은 형태의 테이블
   3. 계산(최단거리)
   
+ First Choice
   1. 언덕등반 + mutation(임의의 자료, noise)
   2. 검색 횟수가 정해져있는 전역검색
