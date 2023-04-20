import pygame
import gfx
from util import *
from algo_info import *
import threading

# 0. 알고리즘 만들기
## 0-1. 포팅(porting)
# 1. 좌표찍기
## 1-1. p를 랜덤으로 만듦(답이 있는 랜덤)
# 2. 루프 만들기
## 2-1. 알고리즘 배치
# 3. 그래프 그리기
## 3-1.점, 선, 텍스트 그리기
### draw_point(x,y) => void
### draw_line(x,y) => void
### draw_text(x,y) => void

def loop():
    # 1. 알고리즘 정보를 가져와서
    for i in range(len(ALGO_INFO)):
        print(ALGO_INFO[i])

    # 2. 계속해서 그림
    while True:
        gfx.check_events()

        # gfx.draw_text_center(surface, "Hello", font, 50, 50)
        gfx.draw_dividers(surface, DRIVERS)

        for i in range(len(ALGO_INFO)):
            if i < len(sim):
                gfx.draw_text_top_left(surface, ALGO_INFO[i]["name"], GREEN, font, *ALGO_INFO[i]["name_coords"])
                gfx.draw_path(surface, list_of_cities_list[i], sim[i].best_order)
            elif len(sim[ALGO_INFO[i]["depends"]].best_order !=0) :
                # 쓰레드에서 에러, 수정 필요
                pass

        pygame.display.update()
        surface.fill(BLACK)



pygame.init()
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
font = pygame.font.SysFont("Consolas", FONT_HEIGHT)

cities = make_cities(20)
# graph = make_graph_from_city_list(cities)
list_of_cities_list = []
sim = []
threads = []

# 풀어서 객체 만들기
for i in range(len(ALGO_INFO)):
    list_of_cities_list.append(displace(cities, *ALGO_INFO[i]["displacement"])) # 해체구문(*)

# 브루트포스 thread 돌기 (쓰레드 에러 => 동기적으로 이뤄지지 않음)
for i in range(len(ALGO_INFO)):
    if ALGO_INFO[i]["depends"] == -1:
        sim.append(ALGO_INFO[i]["sim"](list_of_cities_list[i])) # 즉시실행함수
        threads.append(threading.Thread(target=sim[i].find))
        threads[i].daemon = True

# localsearch는 비thread로 돌기


if __name__ == "__main__":
    # initialize the pygame module
    pygame.display.set_caption("TSP - Visualizer")
    loop()
    # print(cities)