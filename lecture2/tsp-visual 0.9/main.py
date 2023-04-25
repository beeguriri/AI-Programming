import os
import pygame
import gfx
import threading

from util import *
from algoritms import LocalSearch
from algo_info import ALGO_INFO, DIVIDERS


def loop():
    for i in range(len(ALGO_INFO)):
        if ALGO_INFO[i]["depends"] == -1:
            threads[i].start()

    while True:
        gfx.check_events()

        for i in range(len(ALGO_INFO)):
            if i < len(sims):
                gfx.draw_text_top_left(
                    surface,
                    ALGO_INFO[i]["name"],
                    GREEN,
                    font,
                    *ALGO_INFO[i]["name_coords"]
                )
                # print(ALGO_INFO[i]["name"], sims[i].best_order)
                gfx.draw_path(surface, list_of_cities_list[i], sims[i].best_order)
                gfx.draw_text_top_left(
                    surface,
                    "Path Length : " + str(sims[i].best_distance),
                    WHITE,
                    font,
                    *ALGO_INFO[i]["length_coords"]
                )
            elif len(sims[ALGO_INFO[i]["depends"]].best_order) != 0:
                for j in range(len(ALGO_INFO)):
                    if ALGO_INFO[j]["depends"] != -1:
                        if ALGO_INFO[j]["sim"] == LocalSearch.LocalSearchSolver:
                            sims.append(
                                ALGO_INFO[j]["sim"](
                                    list_of_cities_list[j],
                                    sims[ALGO_INFO[j]["depends"]].best_order[:],
                                    int(ALGO_INFO[j]["name"][-1]),
                                )
                            )
                        else:
                            sims.append(
                                ALGO_INFO[j]["sim"](
                                    list_of_cities_list[j],
                                    sims[ALGO_INFO[j]["depends"]].best_order[:],
                                )
                            )
                        threads.append(threading.Thread(target=sims[j].find))
                        threads[j].daemon = True
                        threads[j].start()
        gfx.draw_dividers(surface, DIVIDERS)
        pygame.display.update()
        surface.fill(BLACK)


os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (WINDOW_X, WINDOW_Y)
pygame.init()
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption("TSP-Visualizer")
font = pygame.font.SysFont("Malgun Gothic", FONT_HEIGHT)

cities = make_cities(30)
list_of_cities_list = []
sims = []
threads = []

for i in range(len(ALGO_INFO)):
    list_of_cities_list.append(displace(cities, *ALGO_INFO[i]["displacement"]))

for i in range(len(ALGO_INFO)):
    if ALGO_INFO[i]["depends"] == -1:
        sims.append(ALGO_INFO[i]["sim"](list_of_cities_list[i]))
        threads.append(threading.Thread(target=sims[i].find))
        threads[i].daemon = True


if __name__ == "__main__":
    loop()
