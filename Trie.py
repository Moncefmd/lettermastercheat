from Node import Node


class Trie:
    def __init__(self):
        self.root = Node("*")

    def add_string(self, word):
        curnode = self.root
        for letter in word:
            temp = curnode.get_child(letter)
            if temp is not None:
                curnode = temp
            else:
                curnode.add_child(letter)
                curnode = curnode.get_child(letter)
        curnode.add_child(".")

    def contains(self, word):
        curnode = self.root
        for letter in word:
            temp = curnode.get_child(letter)
            if temp is not None:
                curnode = temp
            else:
                return False
        temp = curnode.get_child(".")
        return temp is not None

