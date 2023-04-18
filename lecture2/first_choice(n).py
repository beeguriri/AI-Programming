import random
import numeric

# 탐색 횟수의 제한은 반드시 걸어줘야함
# 지역최적화를 할 때
# 전역을 100번 이내에 검색해서 최적점을 찾겠다!
LIMITS = 100


def first_choice(p):
    current = numeric.random_init(p)
    # 최적값임을 상정하고
    value_distance = numeric.evaluate(current, p)
    ## 알고리즘을 활용하여 최적값을 변경
    i = 0
    while i < LIMITS:
        return

    return current, value_distance


def random_mutant(current, p):
    DELTA = 0.01
    # delta값 구간 안에 어떤 값을 가져오면 됨
    delta = [-DELTA, DELTA]
    d = random.choice(delta)
    return d


def inversion(current, i, j):
    pass


if __name__ == '__main__':
    p = tsp.create_problem('./data/Convex.txt')
    solution, minimum = first_choice(p)
    print(solution)
    print(minimum)