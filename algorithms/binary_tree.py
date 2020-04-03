class Node:
    label = None
    left = None
    right = None

    def __init__(self, label):
        self.label = label

    def add(self, label):
        if label < self.label:
            if self.left == None:
                self.left = Node(label)
            else:
                self.left.add(label)
        elif label > self.label:
            if self.right == None:
                self.right = Node(label)
            else:
                self.right.add(label)
    
    def visit(self, tree):
        if self.left != None:
            self.left.visit(tree)

        tree.append(self.label)
        
        if self.right != None:
            self.right.visit(tree)

    def search(self, label):
        if label == self.label:
            return self

        if label < self.label and self.left is not None:
            return self.left.search(label)

        if label > self.label and self.right is not None:
            return self.right.search(label)

        return None
            

class BinaryTree:
    root = None

    def add(self, label):
        if self.root == None :
            self.root = Node(label)
        else :
            self.root.add(label)

    def traverse(self):
        tree = []

        if self.root != None:
            self.root.visit(tree)
        
        return tree

    def search(self, label):
        return self.root.search(label)