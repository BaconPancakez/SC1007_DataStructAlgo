class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def findNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
        if self.head is None:
            raise ValueError("List is empty")

        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur

    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True

        prev_node = self.findNode(index - 1)
        if prev_node is not None:
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.size += 1
            return True
        return False

    def removeNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")

        if self.head is None:
            return False

        if index == 0:
            cur = self.head
            self.head = cur.next
            self.size -= 1
            return True

        pre = self.findNode(index - 1)
        if pre is not None and pre.next is not None:
            cur = pre.next
            pre.next = cur.next
            self.size -= 1
            return True
        return False

    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")


def interleaveQueue(head):
    # Write your code here #
    if not head or not head.next:
        return head
    slow, fast = head, head
    prev = None

    # Find the middle node
    while fast and fast.next:
        prev = slow
        fast = fast.next.next
        slow = slow.next

    prev.next = None
    second_half = slow

    # Reverse 2nd Half
    prev = None
    while second_half:
        temp = second_half.next
        second_half.next = prev
        prev = second_half
        second_half = temp
    second_half = prev

    # Merge two half together
    first_half = head
    while first_half and second_half:
        firstNode, secondNode = first_half.next, second_half.next
        first_half.next = second_half
        if first_half:
            second_half.next = firstNode
        first_half, second_half = firstNode, secondNode
    return head


if __name__ == "__main__":
    linked_list = LinkedList()

    print("Enter a list of numbers, terminated by any non-digit character: ", end="")
    input_string = input()
    numbers = input_string.split()

    counter = 0
    for num in numbers:
        try:
            linked_list.insertNode(int(num), counter)
            counter += 1
        except ValueError:
            break

    print("\nBefore:", end=" ")
    linked_list.printList()
    linked_list.head = interleaveQueue(linked_list.head)
    print("After:", end=" ")
    linked_list.printList()
