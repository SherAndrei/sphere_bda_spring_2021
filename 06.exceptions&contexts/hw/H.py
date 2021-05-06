from collections import deque
import string


class Node:
    def __init__(self, character="", word=None, is_key=False, parent=None):
        self.character = character
        self.is_key = is_key
        self.parent = parent
        if self.is_key:
            self.word = word
        self.children = dict()

    def add_child(self, node):
        self.children[node.character] = node


class Trie:
    def __init__(self):
        self.head = Node("")
        self.length = 0

    def find_max_prefix(self, word):
        current_parent = self.head
        max_prefix = ""
        for ch in word:
            find_node = False
            for character, child in current_parent.children.items():
                if ch == character:
                    current_parent = child
                    max_prefix += ch
                    find_node = True
                    break

            if not find_node:
                break

        return max_prefix, current_parent

    def starts_with(self, prefix):
        max_prefix, node = self.find_max_prefix(prefix)
        if len(max_prefix) != len(prefix):
            return TrieIterator(Node())
        return TrieIterator(node)

    def add(self, word):
        max_prefix, node = self.find_max_prefix(word)
        index = len(max_prefix)
        if index == len(word) and node.is_key:
            return
        current_parent = node
        for ch in word[index:]:
            child = Node(ch, parent=current_parent)
            current_parent.add_child(child)
            current_parent = child
        current_parent.is_key = True
        current_parent.word = word
        self.length += 1

    def pop(self, word):
        max_prefix, node = self.find_max_prefix(word)

        if len(max_prefix) != len(word) or not node.is_key:
            raise KeyError(word)
        else:
            if len(node.children) != 0:
                node.is_key = False
                node.word = None
            else:
                node.parent.children.pop(node.character)
                node = node.parent
                while (len(node.children) == 0 and not node.is_key
                       and node.parent is not None):
                    node.parent.children.pop(node.character)
                    node = node.parent
            self.length -= 1

    def __contains__(self, word):
        max_prefix, node = self.find_max_prefix(word)
        return len(max_prefix) == len(word) and node.is_key

    def __iter__(self):
        return TrieIterator(self.head)

    def __len__(self):
        return self.length


class TrieIterator:
    def __init__(self, head):
        self.sorted_string = "{}{}{}".format(
            string.digits,
            string.ascii_uppercase,
            string.ascii_lowercase)
        self.queue = deque([head])

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.queue) != 0:
            node = self.queue.popleft()
            for character in self.sorted_string:
                if character in node.children:
                    child = node.children[character]
                    self.queue.append(child)
            if node.is_key:
                return node.word
        raise StopIteration
