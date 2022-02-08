import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.n = []
        self.parent = None
    def set_parent(self, parent):
        self.parent = parent
    def add(self, node):
        self.n.append(node)

class Stack:
    def __init__(self):
        self.s = []
    def add(self, node):
        self.s.append(node)
    def get(self):
        node = self.s[len(self.s)-1]
        self.s = self.s[:len(self.s)-1]
        return node
    def isempty(self):
        if len(self.s) == 0:
            return True
        return False

class Explore(Stack):
    def get(self):
        pass
    def check(self, node):
        if node in self.s:
            return True
        return False

def dfs(root, find):
    temp = root
    s = Stack()
    e = Explore()
    s.add(temp)
    temp.set_parent(None)
    steps = []

    while True:
        if s.isempty():
            print("No solution!!")
            sys.exit(0)
        
        temp = s.get()
        if e.check(temp):
            continue

        steps.append(temp.val)

        e.add(temp)

        for i in temp.n:
            if e.check(i):
                continue
            i.set_parent(temp)
            if i == find:
                temp = i
                print("Soluiton Found:")
                find_path(temp)
                print(steps) 
                sys.exit(2)
            s.add(i)

def find_path(node):
    temp = node
    path = []

    while temp != None:
        path.append(temp.val)
        temp = temp.parent
    path.reverse()
    print(path)


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    a.n = [b, c, d, g]
    b.n = [a, h]
    c.n = [a, e]
    d.n = [a, f]
    e.n = [c, f]
    f.n = [d, e, h]
    g.n = [a]
    h.n = [f, b]
    dfs(g, h) 