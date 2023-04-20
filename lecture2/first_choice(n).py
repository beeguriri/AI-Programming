import random
import numeric

# 탐색 횟수의 제한은 반드시 걸어줘야함
# 지역최적화를 할 때
# 전역을 100번 이내에 검색해서 최적점을 찾겠다!
LIMITS = 100


def first_choice(p):
    # 최적값임을 상정하고
    current = random_init(p)
    values = evaluate(current, p)
    ## 알고리즘을 활용하여 최적값을 변경
    i = 0
    while i < LIMITS:
        successor = random_mutant(current, p)
        value_eval = evaluate(successor, p)
        if value_eval < values:
            current = successor
            values = value_eval
            i = 0
        else:
            i += 1
    return current, values


def random_mutant(current, p):
    i = random.randint(0, len(current) - 1)
    DELTA = 0.01
    # delta값 구간 안에 어떤 값을 가져오면 됨
    delta = [-DELTA, DELTA]
    d = random.choice(delta)
    return mutate(current, i, d, p)

def display_setting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

def inversion(current, i, j):
    pass


if __name__ == '__main__':
    p = tsp.create_problem('./data/Convex.txt')
    solution, minimum = first_choice(p)
    describe_problem(p)
    display_setting()
    display_result(solution, minimum)