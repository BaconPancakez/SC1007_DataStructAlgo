class Node:
    def __init__(self, y):
        self.data = y
        self.left = None
        self.right = None


def printPreOrder(node):
    if node is None:
        return

    print(node.data, end=' ')
    printPreOrder(node.left)
    printPreOrder(node.right)


def printInOrder(node):
    if node is None:
        return

    printInOrder(node.left)
    print(node.data, end=' ')
    printInOrder(node.right)


def printPostOrder(node):
    if node is None:
        return
    printPostOrder(node.left)
    printPostOrder(node.right)
    print(node.data, end=' ')


def printSum(node):

    if node is None:
        return 0

    if node.data % 2 == 0:
        sum_even = node.data

    else:
        sum_even = 0

    return sum_even + printSum(node.left) + printSum(node.right)

    # Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    # Function call
    print("Preorder traversal of binary tree is:")
    printPreOrder(root)

    print("\nInOrder traversal of binary tree is:")
    printInOrder(root)

    print("\nPostOrder traversal of binary tree is:")
    printPostOrder(root)

    print("\nSum of even nodes: ")
    print(printSum(root))
