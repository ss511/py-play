"""
Lowest Common Ancestor in a Binary Tree

Given a binary tree (not a binary search tree) and two values say n1 and n2,
write a program to find the least common ancestor.

"""


class Node:
    # Constructor to create a new binary node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_lca(node, val1, val2):
    if node is None:
        return None
    if node.data == val1 or node.data == val2:
        return node

    left_lca = find_lca(node.left, val1, val2)
    right_lca = find_lca(node.right, val1, val2)

    if left_lca and right_lca:
        return node
    return left_lca if right_lca is None else right_lca


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("LCA(4, 5) = %d" % find_lca(root, 4, 5).data)
    print("LCA(4, 6) = %d" % find_lca(root, 4, 6).data)
    print("LCA(3, 4) = %d" % find_lca(root, 3, 4).data)
    print("LCA(2, 4) = %d" % find_lca(root, 2, 4).data)
    print("LCA(3, 7) = %d" % find_lca(root, 3, 7).data)
    print("LCA(6, 7) = %d" % find_lca(root, 6, 7).data)


