# First-Choice
# 간단한 언덕 등반 알고리즘
## > Convex.txt를 사용해서 계산

import random

## > 1. 파일 읽기
def create_problem(filename):
    # 1-1. 파일 읽기
    ini_file = open(filename, 'r')

    # 1-2. 수식과 리스트로 분리
    expression = ini_file.readline().strip()

    var_names = []
    low = []
    up = []
    for line in ini_file.readlines() :
        var_names.append(line.split(',')[0])
        low.append(float(line.split(',')[1]))
        up.append(float(line.split(',')[2]))
    ini_file.close()
    domain = [var_names, low, up]

    # 1-3. return
    return (expression, domain)

## > 2. 초기값 생성 -> 유니폼(정규분포) 랜덤
#### 매개변수는 튜플을 쓰자(immutable)
def random_init(p):
    expression, domain = p
    init = []
    for i in range(0, len(domain[0])):
        # 최대 최소 사이의 랜덤값
        init.append(random.uniform(domain[1][i], domain[2][i]))
    return init

## > 3. 계산!
def evaluate(state, p):
    num_eval = 0 #초기값 설정
    expression = p[0]
    var_name = p[1][0]

    for i in range(len(var_name)):
        assignment = var_name[i] + '=' + str(state[i])
        exec(assignment) # exec : String type의 문장을 python code로 실행시켜 줌

    return eval(expression) # eval : String type 의 식 // 사용금지(ㅋㅋ)


if __name__ == '__main__':
    pass

