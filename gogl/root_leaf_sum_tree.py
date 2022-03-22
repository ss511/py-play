"""
Sum of all the numbers that are formed from root to leaf paths

Given a binary tree, where every node value is a Digit from 1-9 .Find the sum of all the numbers which are formed from root to leaf paths.
For example consider the following Binary Tree.

         6
       /      \
     3          5
   /   \          \
  2     5          4
      /   \
     7     4
  There are 4 leaves, hence 4 root to leaf paths:
   Path                    Number
  6->3->2                   632
  6->3->5->7               6357
  6->3->5->4               6354
  6->5>4                    654
Answer = 632 + 6357 + 6354 + 654 = 13997
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_sum(root):
    nums = []
    pre_order(root, 0, nums)
    print(nums)
    return sum(nums)


def pre_order(root, num, nums):
    if root is None:
        return
    num = num*10 + root.data
    if root.left is None and root.right is None:
        nums.append(num)
        return
    pre_order(root.left, num, nums)
    pre_order(root.right, num, nums)


if __name__ == "__main__":
    tree = Node(6)
    tree.left = Node(3)
    tree.right = Node(5)
    tree.left.left = Node(2)
    tree.left.right = Node(5)
    tree.left.right.left = Node(7)
    tree.left.right.right = Node(4)
    tree.right.right = Node(4)

    print(get_sum(tree))
