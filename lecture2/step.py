import numpy as np


def compute_error_for_line_given_points(b, m, points):
    total_error = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(len(points))


def step_gd(current_b, current_m, points, lr):

    b_gradient = 0
    m_gradient = 0

    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i,0]
        y = points[i,1]

        # 오차를 최소로 구하고자 함(m_gradient를 최대로 만듦)
        # 부호 확인
        b_gradient += -(2/N)*(y-((current_m*x)+current_b))
        m_gradient += -(2/N)*x*(y-((current_m*x)+current_b))

    new_b = current_b - (lr*b_gradient)
    new_m = current_m - (lr*m_gradient)

    return [new_b, new_m]


# 확률적 경사하강법
def gd(points, st_b, st_m, lr, iter):
    b = st_b
    m = st_m
    for i in range(iter):
        b, m = step_gd(b, m, np.array(points), lr)
    return [b, m]


if __name__ == "__main__":
    #pandas 없이 csv 읽기
    points = np.genfromtxt("./data/data.csv", delimiter=",")

    # 경사하강법 : 학습률, 절편, 기울기
    learning_rate = 0.0001
    init_b = 0
    init_m = 0

    # 반복 횟수 결정
    num_iter = 1000

    # 알고리즘 만들기
    print(
        f"Starting gradient descent at b = {init_b}, m = {init_m}, error = {compute_error_for_line_given_points(init_b, init_m, points)}"
    )
    print("...Running...")
    [b,m] = gd(points, init_b, init_m, learning_rate, num_iter)
    print(f"b={b}, m={m}, error = {compute_error_for_line_given_points(b, m, points)}")

    # 시각화

    #