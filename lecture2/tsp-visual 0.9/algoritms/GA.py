import random
from util import *


class GASolver:
    def __init__(self, cities, given_order=[]):
        self.cities = cities
        self.total = len(cities)
        self.best_order = []
        self.best_distance = float("inf")
        self.population = []
        self.fitness = []
        self.mutation_rate = 0.01
        self.pop_size = 1000
        self.gen_num = 0
        order = []

        if len(given_order) == 0:
            for i in range(self.total):
                order.append(i)
            for i in range(self.pop_size):
                p = order[:]
                random.shuffle(p)
                self.population.append(p)
        else:
            order = given_order
            for i in range(self.pop_size - 1):
                p = order[:]
                indexA = random.randrange(len(p))
                indexB = random.randrange(len(p))
                p[indexA], p[indexB] = p[indexB], p[indexA]
                self.population.append(p)
            self.population.append(given_order)

        if len(given_order) != 0:
            self.population[random.randrange(0, self.pop_size)] = given_order

        for i in range(self.pop_size):
            d = calc_path_distance(self.cities, self.population[i])
            if d < self.best_distance:
                self.best_distance = d
                self.best_order = self.population[i]
            self.fitness.append(1 / (d + 1))

    def mutate(self, order, mutation_rate):
        for i in range(len(order)):
            if random.random() < mutation_rate:
                index_a = random.randrange(len(order))
                index_b = (index_a + 1) % len(order)
                order[index_a], order[index_b] = order[index_b], order[index_a]

        return order


    def cross_over(self, order_A, order_B):
        start = random.randrange(len(order_A))
        end = random.randrange(len(order_B))
        if start > end:
            start, end = end, start
        order = order_A[start:end]

        for pos in order_B:
            if pos not in order:
                order.append(pos)

        return order


    def cross_over2(self, order_A, order_B):
        pass


    def calc_fitness(self):
        for i in range(self.pop_size):
            d = calc_path_distance(self.cities, self.population[i])
            if d < self.best_distance:
                self.best_distance = d
                self.best_order = self.population[i]
            self.fitness[i] = 1 / (d**8 + 1)


    def normalize_fitness(self):
        total_fit = sum(self.fitness)
        for i in range(len(self.fitness)):
            self.fitness[i] /= total_fit


    def make_next_population(self):
        # 초기값 생성
        self.gen_num += 1
        # 파이썬 구문 (list 선언 -> for loop -> 결과 append -> list 리턴)
        new_pop = []
        for i in range(self.pop_size):
            order_a = random.choices(self.population, weights=self.fitness, k=1)[0][:]
            order_b = random.choices(self.population, weights=self.fitness, k=1)[0][:]
            while order_b == order_a:
                order_b = random.choices(self.population, weights=self.fitness, k=1)[0][:]
            order = self.cross_over(order_a, order_b)
            order = self.mutate(order, self.mutation_rate)
            new_pop.append(order)
        self.population = new_pop

    def find(self):
        while True:
            # best_order 경로가 포함 되길 원함
            self.make_next_population()
            self.calc_fitness()
            self.normalize_fitness()
