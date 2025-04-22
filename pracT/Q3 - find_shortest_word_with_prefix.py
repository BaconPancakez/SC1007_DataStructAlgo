class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.first_child = None
        self.next_sibling = None
        self.is_end_of_word = False


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # Add to the end

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove from the front
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def _find_child(node, char):
    current = node.first_child
    while current:
        if current.char == char:
            return current
        current = current.next_sibling
    return None


def _add_child(node, char):
    new_node = TrieNode(char)
    new_node.next_sibling = node.first_child
    node.first_child = new_node
    return new_node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            child = _find_child(node, char)
            if not child:
                child = _add_child(node, char)
            node = child
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            node = _find_child(node, char)
            if not node:
                return False
        return node.is_end_of_word

    def find_shortest_word(self):  # question 3
        # Traverse to the end of the prefix
        node = self.root

        # Use BFS
        queue = Queue()
        queue.enqueue((node, 0))
        min_depth = None
        count = 0

        while not queue.is_empty():
            node, depth = queue.dequeue()
            if node.is_end_of_word:
                if min_depth is None:
                    min_depth = depth
                if depth == min_depth:
                    count += 1
                elif min_depth < depth:
                    break
            child = node.first_child
            while child:
                queue.enqueue((child, depth + 1))
                child = child.next_sibling
        return count


trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("care")
trie.insert("cane")
trie.insert("camera")
trie.insert("campus")
trie.insert("camp")
trie.insert("dog")
trie.insert("dot")

print(f"Number of shorted word is ",
      trie.find_shortest_word())
