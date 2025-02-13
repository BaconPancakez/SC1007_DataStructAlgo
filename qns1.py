class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def printList(self):
        cur = self.head
        if not cur:
            print("Empty")
            return
        while cur:
            print(cur.item, end=" ")
            cur = cur.next
        print()

    def findNode(self, index):
        if index < 0 or index >= self.size:
            return None
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur

    def insertNode(self, index, value):
        if index < 0 or index > self.size:  # Allow inserting at the end
            return -1

        newNode = ListNode(value)
        if index == 0:
            # Insert at head
            newNode.next = self.head
            self.head = newNode
        else:
            # Insert in between
            prev = self.findNode(index - 1)
            newNode.next = prev.next
            prev.next = newNode

        self.size += 1
        return 0

    def removeNode(self, index):
        if index < 0 or index >= self.size:
            return -1
        if index == 0:  # Remove first node
            self.head = self.head.next
        else:  # Remove subsequent nodes
            prev = self.findNode(index - 1)
            prev.next = prev.next.next
        self.size -= 1
        return 0

    def moveEvenItemsToBack(ll):
        if ll.size < 2:
            return
        cur = ll.head
        index = 0
        for _ in range(ll.size):
            if cur.item % 2 == 0:
                even_value = cur.item
                cur = cur.next
                ll.removeNode(index)
                ll.insertNode(ll.size, even_value)
            else:
                cur = cur.next
                index += 1
        return 0


if __name__ == "__main__":
    ll = LinkedList()

    while True:
        print("1: Insert an integer to the linked list")
        print("2: Move all even integer to the back")
        print("0: Quit")

        choice = int(input("Please input your choice (1/ 2/ 0): "))

        if choice == 1:
            value = int(input("Enter integer: "))
            ll.insertNode(ll.size, value)  # Insert at the end
            print("The resulting Linked list is")
            ll.printList()
        elif choice == 2:
            moveEvenItemsToBack(ll)
            print("The resulting Linked list is")
            ll.printList()
        elif choice == 0:
            ll.removeAllItems()
            break
        else:
            print("Choice unknown. Please enter a valid choice.")
