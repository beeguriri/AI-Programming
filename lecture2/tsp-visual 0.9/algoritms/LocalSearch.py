import itertools
from util import *


class LocalSearchSolver:
    def __init__(self, cities, order, d):
        self.cities = cities
        self.total = len(cities)
        self.best_order = order[:]
        self.best_distance = calc_path_distance(self.cities, self.best_order)
        self.d = d

    def foo(self, bestO, bestD):
        pass

    def find(self):
        pass