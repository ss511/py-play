"""
Convert a given tree to its Sum Tree

Given a Binary Tree where each node has positive and negative values.
Convert this to a tree where each node contains the sum of the left and right sub trees in the original tree.
The values of leaf nodes are changed to 0.

For example, the following tree
                  10
               /      \
             -2        6
           /   \      /  \
         8     -4    7    5
should be changed to

                 20(4-2+12+6)
               /      \
         4(8-4)      12(7+5)
           /   \      /  \
         0      0    0    0
"""


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def convert_to_sum_tree(node):
    if node is None:
        return 0
    curr = node.data
    node.data = convert_to_sum_tree(node.left) + convert_to_sum_tree(node.right)
    return curr + node.data


def pre_order(node):
    if node is None:
        return
    print(node.data, end=" ")
    pre_order(node.left)
    pre_order(node.right)


if __name__ == "__main__":
    root = Tree(10)
    root.left = Tree(-2)
    root.right = Tree(6)
    root.left.left = Tree(8)
    root.left.right = Tree(-4)
    root.right.left = Tree(7)
    root.right.right = Tree(5)
    pre_order(root)
    print()
    convert_to_sum_tree(root)
    pre_order(root)