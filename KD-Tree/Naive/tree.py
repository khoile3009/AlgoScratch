from data import generate_data_points
from node import Node
import matplotlib.pyplot as plt


class KDTree:
    def __init__(self, k=2, initial_data=None):
        self.k = k
        self.root: Node = None
        if initial_data is not None:
            print(initial_data)
            self.__dimension_check(initial_data)
            for i in range(initial_data.shape[0]):
                point = initial_data[i, :]
                if not self.root:
                    self.root = Node(point, 0)
                else:
                    self.root.add_child(point)

    def __dimension_check(self, data):
        if self.k != data.shape[1]:
            raise ValueError("Wrong number of dimension")

    def print_tree(self):
        self.root.traverse(func=lambda node: print(
            node.value, node.split_index))

    def draw_tree(self):
        self.root.traverse(func=lambda node: node.draw())
        plt.show()


if __name__ == '__main__':
    data = generate_data_points(2, 10)
    tree = KDTree(2, data)
    tree.draw_tree()
