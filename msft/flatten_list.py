"""
Given a linked list where every node represents a linked list and contains two pointers of its type:
(i) Pointer to next node in the main list (we call it ‘right’ pointer in the code below)
(ii) Pointer to a linked list where this node is headed (we call it the ‘down’ pointer in the code below).
All linked lists are sorted. See the following example

       5 -> 10 -> 19 -> 28
       |    |     |     |
       V    V     V     V
       7    20    22    35
       |          |     |
       V          V     V
       8          50    40
       |                |
       V                V
       30               45
Write a function flatten() to flatten the lists into a single linked list.
The flattened linked list should also be sorted.
For example, for the above input list, output list should be 5->7->8->10->19->20->22->28->30->35->40->45->50.
"""


class List:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None


def merge(a, b):
    if a is None:
        return b

    if b is None:
        return a

    if a.data < b.data:
        result = a
        result.down = merge(a.down, b)
    else:
        result = b
        result.down = merge(a, b.down)
    result.right = None
    return result


def flatten(node):
    if node is None or node.down is None and node.right is None:
        return node

    node.right = flatten(node.right)
    node = merge(node, node.right)

    return node


if __name__ == "__main__":
    head = List(5)
    head.right = List(10)
    head.down = List(7)
    head.down.down = List(8)
    head.down.down.down = List(30)
    head.right.down = List(20)
    head.right.right = List(19)
    head.right.right.down = List(22)
    head.right.right.down.down = List(50)
    head.right.right.right = List(28)
    head.right.right.right.down = List(35)
    head.right.right.right.down.down = List(40)
    head.right.right.right.down.down.down = List(45)

    head = flatten(head)

    while head is not None:
        print(head.data)
        head = head.down
