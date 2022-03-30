"""
Given a Binary Search Tree (BST) and a range, count number of nodes that lie in the given range.

Examples:
Input:
        10
      /    \
    5       50
   /       /  \
 1       40   100
Range: [5, 45]

Output:  3
There are three nodes in range, 5, 10 and 40

"""


class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_node_count(root, lower, upper):
    if root is None:
        return 0
    if root.data == lower and root.data == upper:
        return 1

    if lower <= root.data <= upper:
        return 1 + get_node_count(root.left, lower, upper) + get_node_count(root.right, lower, upper)
    elif root.data < lower:
        return get_node_count(root.right, lower, upper)
    else:
        return get_node_count(root.left, lower, upper)


if __name__ == "__main__":
    root1 = BST(10)
    root1.left = BST(5)
    root1.right = BST(50)
    root1.left.left = BST(1)
    root1.right.left = BST(40)
    root1.right.right = BST(100)

    rl1 = 5
    rh1 = 45

    rl2 = 40
    rh2 = 50

    rl3 = 60
    rh3 = 120

    rl4 = 120
    rh4 = 150

    print(get_node_count(root1, rl1, rh1))
    print(get_node_count(root1, rl2, rh2))
    print(get_node_count(root1, rl3, rh3))
    print(get_node_count(root1, rl4, rh4))