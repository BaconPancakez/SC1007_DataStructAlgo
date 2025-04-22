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

    def collect_all_words(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)
        child = node.first_child
        while child:
            self.collect_all_words(child, prefix + child.char, results)
            child = child.next_sibling

    def find_words_with_prefix(self, prefix):  # question 2
        results = []
        node = self.root

        for char in prefix:
            node = _find_child(node, char)
            if not node:
                return []

        self.collect_all_words(node, prefix, results)
        return results


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

prefix1 = "ca"
prefix2 = "do"
prefix3 = "z"
print(f"Words starting with '{prefix1}': ",
      trie.find_words_with_prefix(prefix1))
print(f"Words starting with '{prefix2}':",
      trie.find_words_with_prefix(prefix2))
print(f"Words starting with '{prefix3}':",
      trie.find_words_with_prefix(prefix3))
