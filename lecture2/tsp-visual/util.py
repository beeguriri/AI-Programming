import random
import pygame


# 상수 변수는 밖으로 뺀다
WIDTH = 300
HEIGHT = 300
FONT_HEIGHT = 20

WINDOW_WIDTH = WIDTH * 4
WINDOW_HEIGHT = (HEIGHT + FONT_HEIGHT + FONT_HEIGHT) * 2    # 높이 + 아래위 캡션
WINDOW_X = 10
WINDOW_Y = 10

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

CITY_SIZE = 300
MIN_CITY_SIZE = 7.5
MAX_CITY_SIZE = 10

def make_cities(total_cities):
    cities = []
    r = CITY_SIZE // total_cities
    for i in range(total_cities):
        cities.append(pygame.math.Vector2(random.randrange(r, WIDTH-r),
                                          random.randrange(r, HEIGHT-r)))

    return cities


def make_graph_from_city_list(cities):
    n = len(cities)
    graph = [[0 for i in range(n)] for j in range(n)] # 중복루프

    for i in range(n):
        city_a = cities[i]
        for j in range(i, n): #주대각선 위쪽만큼 계산
            if i==j:
                graph[i][j]==0 #주대각선은 0
            else:
                city_b = cities[j]
                d = (city_a - city_b).length()
                graph[i][j] = graph[j][i] = d
    return graph


def calc_path_distance(points, order):
    for i in range(len(order)):
        city_a = points[order[i%len(order)]]
        city_b = points[order[(i+1)%len(order)]]
        d = (city_a - city_b).length()
        dist += d

    return dist


def displace(cities, x, y):
    new = []
    displaceVector = pygame.math.Vector2(x,y)
    for c in cities:
        new.append(c + displaceVector)

    return new
















