class Node(object):
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
class LinkedList(object):
    def __init__(self) -> None:
        self.head = None
    def add(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        val = self.head
        while val!=None:
            if val.right==