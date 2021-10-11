import numpy as np
import matplotlib.pyplot as plt

MAX_LIM = 100


class Node:

    def __init__(self, value, split_index: int, min_lim=0, max_lim=100):
        self.min_lim = min_lim
        self.max_lim = max_lim
        self.value = value
        self.split_index = split_index
        self.__check_index(value, split_index)
        self.left: Node = None
        self.right: Node = None

    def add_child(self, point):
        if point[self.split_index] >= self.value[self.split_index]:
            self.__add_right(point)
        else:
            self.__add_left(point)

    def __add_left(self, point):
        if self.left:
            self.left.add_child(point)
        else:
            self.left = Node(point, self.__get_next_split_index(),
                             max_lim=self.value[self.split_index])

    def __add_right(self, point):
        if self.right:
            self.right.add_child(point)
        else:
            self.right = Node(point, self.__get_next_split_index(),
                              min_lim=self.value[self.split_index])

    def __get_next_split_index(self):
        if self.value.shape[0] - 1 == self.split_index:
            return 0
        else:
            return self.split_index + 1

    def __check_index(self, point, split_index):
        if point.shape[0] <= split_index:
            raise ValueError('Index is larger than data dimension')

    def traverse(self, func):
        func(self)
        if self.left:
            self.left.traverse(func)
        if self.right:
            self.right.traverse(func)

    # Only for visualize 2d tree
    def draw(self):
        plt.scatter(self.value[0], self.value[1])
        if self.split_index == 0:
            plt.plot((self.value[0], self.value[0]),
                     (self.min_lim, self.max_lim))
        else:
            plt.plot((self.min_lim, self.max_lim),
                     (self.value[1], self.value[1]))
