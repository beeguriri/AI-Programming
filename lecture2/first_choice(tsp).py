import random
import tsp

# 탐색 횟수의 제한은 반드시 걸어줘야함
# 지역최적화를 할 때
# 전역을 100번 이내에 검색해서 최적점을 찾겠다!
LIMITS = 100

def first_choice(p):
    current = tsp.random_init(p)
    # 최적값임을 상정하고
    value_distance = tsp.evaluate(current, p)
    ## 알고리즘을 활용하여 최적값을 변경
    i = 0
    while i < LIMITS:
        successor = random_mutant(current, p)
        _temp_value_distance = tsp.evaluate(successor, p)
        if _temp_value_distance < value_distance:
            current = successor
            value_distance = _temp_value_distance
            i = 0
        else:
            i += 1
    
    return current, value_distance

# 전역 최적화 기법
def random_mutant(current, p):
    while True:
        i, j = sorted([random.randrange(p[0]) for _ in range(2)])

        # 양쪽을 다 찾고자 함
        if i < j:
            cur_copy = inversion(current, i, j)
            break

    return cur_copy


def inversion(current, i, j):
    cur_copy = current[:]
    while i < j:
        cur_copy[i], cur_copy[j] = cur_copy[j], cur_copy[i]
        i += 1
        j -= 1
    return cur_copy


if __name__ == '__main__':
    p = tsp.create_problem('./data/tsp30.txt')
    solution, minimum = first_choice(p)
    print(solution)
    print(minimum)