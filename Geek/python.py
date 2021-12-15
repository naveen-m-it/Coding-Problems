class tree:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def printTree(self):
        print(self.data)
        print(self.left)
if __name__ == "__main__":
    root = tree(10)
    root.left = tree(5)
    root.right = tree(11)
    root.printTree()