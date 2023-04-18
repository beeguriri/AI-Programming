# tsp문제의 핵심은 시작지점!
# 시작지점을 랜덤으로 사용해서 first choice
# 정답 cost = 890 보다 낮아야한다

import math
import random

# 파일열기
def create_problem(filename):
    f = open(filename, 'r')
    num_cities = int(f.readline())

    locations = []
    for line in f.readlines():
        # 좌표는 튜플(x,y)
        locations.append(eval(line))

    f.close()
    table = create_distance_table(num_cities, locations)

    return num_cities, locations, table

# 인접행렬 만들기
# 간선중심, 간선길이 합 최소
# 맨하튼거리 => 격자(grid world)
# 유클리드거리 => 좌표계
def create_distance_table(num_cities, locations):
    table = []

    for i in range(num_cities):
        line = []
        for k in range(num_cities):
            # 거리 구하기
            distance = math.sqrt((locations[i][0] - locations[k][0])**2 + (locations[i][1] - locations[k][1])**2)
            line.append(distance)
        table.append(line)

    return table

def random_init(p):
    # return : 입력받은 좌표 중 랜덤한 좌표 / shuffle
    n = p[0]
    init = list(range(n))
    random.shuffle(init)
    return init

def evaluate(current, p): # current에는 init 값이 올거
    # cost 출력
    cost = 0
    num_cities, locations, table = p
    for i in range(num_cities): # index 사용
        # 랜덤으로 선택된 좌표의 cost
        cost += table[current[i]][current[i-1]]

    return cost

def describe_problem(p):
    print()
    n = p[0]
    print(f"Number of cities: {n}")

    locations = p[1]
    for i in range(n):
        print(f"{locations[i]}")
        if i%5 == 4:
            print()

    distance = p[2]
    for i in range(n):
        print(f"{distance[i]}")
        if i%5 == 4:
            print()


if __name__ == '__main__':
    p = create_problem('./data/tsp30.txt')
    # describe_problem(p)
    init = random_init(p)
    print(evaluate(init, p))
