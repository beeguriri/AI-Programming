from util import *


class ApproxMSTSolver:
    def __init__(self, cities):
        self.cities = cities
        self.total = len(cities)
        self.best_order = []
        self.best_distance = float("inf")
        self.graph = make_graph_from_city_list(cities)
        self.parent = [None] * self.total

    def min_key(self, key, mst_set):
        mini = float("inf")
        for v in range(self.total):
            if key[v] < mini and mst_set[v] == False:
                mini = key[v]
                min_index = v
        return min_index

    def prim_MST(self):
        key = [float("inf")] * self.total
        key[0] = 0
        mstSet = [False] * self.total
        self.parent[0] = -1
        for _ in range(self.total):
            u = self.min_key(key, mstSet)
            mstSet[u] = True
            for v in range(self.total):
                if (
                    self.graph[u][v] > 0
                    and mstSet[v] == False
                    and key[v] > self.graph[u][v]
                ):
                    key[v] = self.graph[u][v]
                    self.parent[v] = u

    def get_list_of_indices(self, l):
        listOfIndices = []
        for i in range(len(l) + 1):
            indices = []
            for j in range(len(l)):
                if i == l[j]:
                    indices.append(j + 1)
            listOfIndices.append(indices)
        return listOfIndices

    def pre_order(self, l, i, ind):
        if len(l[i]) <= ind:
            return
        for j in range(len(l[i])):
            self.best_order.append(l[i][j])
            self.pre_order(l, l[i][j], 0)

    def find(self):
        self.prim_MST()
        list_of_indices = self.get_list_of_indices(self.parent[1:])
        self.best_order.append(0)
        self.pre_order(list_of_indices, 0, 0)
        self.best_distance = calc_path_distance(self.cities, self.best_order)
