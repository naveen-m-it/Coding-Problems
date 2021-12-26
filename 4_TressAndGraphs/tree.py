class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
if __name__ == "__main__":
    li = Node(3)
    li.insert(10)
    li.insert(20)
    li.insert(5)
    li.insert(13)


