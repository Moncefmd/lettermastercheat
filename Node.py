

class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = []

    def get_child(self, letter):
        val = None
        for x in self.children:
            if x.letter == letter:
                val = x
                break
        return val

    def add_child(self, letter):
        self.children.append(Node(letter))

    def contains(self, letter):
        for e in self.children:
            if e.data == letter:
                return e
        return None

