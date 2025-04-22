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

    def count_words(self, node):  # question 1
        # Can use DFS
        if node.is_end_of_word:
            cnt = 1
        else:
            cnt = 0

        child = node.first_child
        while child:
            cnt += self.count_words(child)
            child = child.next_sibling

        return cnt


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

print("Total words in Trie:", trie.count_words(trie.root))
