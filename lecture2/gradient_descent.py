from numeric import *

DELTA = 0.01
ALPHA = 0.01
EPSILON = 0.0001

# 낮은값의 차이를 가져옴
# 차이가 줄어든다고 가정하고 탐색
def steepest_ascent(p):
    current = random_init(p)
    values = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        (successor, value_best_of) = best_of(neighbors, p)
        if value_best_of >= values:
            break
        else:
            current = successor
            values = value_best_of
    return (current, values)


def mutants(current, p):
    neighbors = []
    for i in range(0, len(current)):
        neighbors.append(mutate(current, i, DELTA, p))
        neighbors.append(mutate(current, i, -DELTA, p))
    return neighbors


def best_of(neighbors, p):
    all = []
    for i in range(0, len(neighbors)):
        all.append(evaluate(neighbors[i], p))
    best_value = min(all)
    best = neighbors[all.index(min(all))]
    return (best, best_value)


def display_setting():
    print()
    print("Search algorithm: Gradient Descent")
    print()
    print(f"Update rate: {ALPHA}")
    print(f"Calculating Derivatives: {EPSILON}")


def gradient(current, p, EPSILON):
    gradient = []

    # 하한과 상한 정하기
    domain = p[1]
    low = domain[1]
    up = domain[2]

    for i in range(len(current)):
        value = current[i]
        derivate = current[:i]
        if(low[i]<= value+EPSILON <=up[i]):
            value = value + EPSILON
        derivate.append(value)
        derivate.extend(current[i+1:])
        gradient.append((evaluate(derivate,p)-value)/EPSILON)

    # 미분(기울기)값 구하기
    # 미분값의 차이 계산
    #
    return gradient


def take_step(current, gradient):   #List - List

    suc = []
    for i in range(len(current)):
        suc.append(current[i] - gradient[i])

    return suc


if __name__ == "__main__":
    p = create_problem("./data/Convex.txt")
    current = random_init(p) # 최대, 최소 사이의 랜덤값
    value = evaluate(current,p)
    while True:
        gradient = gradient(current, p, EPSILON) # List
        next_p = take_step(current, gradient)
        next_n = evaluate(next_p, p)
        if next_n < value:
            current = next_p
            value = next_n
        else:
            break
    print(current, value)
    # solution, minimum = steepest_ascent(p)
    # describe_problem(p)
    # display_setting()
    # display_result(solution, minimum)
