class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None


def insert(root, data):
    if root is None:
        return BSTNode(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def push(stack, node):
    temp = StackNode(node)
    if stack.top is None:
        stack.top = temp
        temp.next = None
    else:
        temp.next = stack.top
        stack.top = temp


def pop(stack):
    if stack.top is not None:
        temp = stack.top
        stack.top = temp.next
        return temp.data
    return None


def is_empty(stack):
    return stack.top is None


def peek(stack):
    if stack.top is not None:
        return stack.top.data
    return None


def postOrderRecursionS1(root):
    # Write your code here #
    # left -> right -> root
    if root is None:
        return
    postOrderRecursionS1(root.left)
    postOrderRecursionS1(root.right)
    print(root.data, end=' ')


def postOrderIterativeS1(root):
    # Write your code here #
    if root is None:
        return

    s = Stack()
    curr = root
    prev = None
    push(s, curr)

    while not is_empty(s):
        curr = peek(s)  # top node

        # Traversal down left tree
        if prev is None or prev.left == curr or prev.right == curr:
            if curr.left is not None:
                push(s, curr.left)
            elif curr.right is not None:
                push(s, curr.right)

        # Back up from left sub tree
        elif curr.left == prev:
            if curr.right is not None:
                push(s, curr.right)

        else:
            print(curr.data, end=' ')
            pop(s)
        prev = curr


if __name__ == "__main__":
    root = None
    choice = 1

    print("1: Insert an integer into the binary search tree")
    print("2: Print the post-order traversal of the binary search tree")
    print("0: Quit")

    while choice != 0:
        choice = int(input("\nPlease input your choice(1/2/0): "))

        if choice == 1:
            value = int(input("Input an integer to insert: "))
            root = insert(root, value)
        elif choice == 2:
            print("Post-order traversal: ", end="")
            postOrderRecursionS1(root)

            print("\nPost-order traversal: ", end="")
            postOrderIterativeS1(root)
            print()
        elif choice == 0:
            break
        else:
            print("Choice unknown")
