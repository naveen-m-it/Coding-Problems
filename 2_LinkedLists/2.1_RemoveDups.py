

class Node(object):

    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList(object):
     
    def __init__(self) -> None:
        self.head = None
    
    def addEnd(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        val = self.head
        while val.next!=None:
            val = val.next
        val.next = newNode
        return
    
    def addBeg(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        return
    
    def size(self):
        if self.head == None:
            return 0
        val = self.head
        count = 0
        while val!=None:
            count+=1
            val = val.next
        return count

    def deleteDups(self):
        val = self.head
        while val!=None:
            s = val
            while s.next!=None:
                if s.next.data == val.data:
                    s.next = s.next.next
                else:
                    s = s.next
            val = val.next
        return

    def popLeft(self):
        if self.head==None:
          return
        if self.head.next ==None:
            self.head = None
            return self.head
        self.head = self.head.next
        return

    def popRight(self):
        if self.size()==1:
            self.head = None
            return self.head
        if self.head == None or self.head.next==None:
            return
        val = self.head
        while val!=None:
            if val.next.next == None:
                val.next = None
                return
            val = val.next

    def printKth(self,k):
        if self.head == None:
            return
        if self.size()<k:
            return
        val = self.head
        while val!=None:
            k-=1
            val = val.next
        print(self.head.data)
        return

    def print(self):
        if self.head == None:
            return
        val = self.head 
        while val!=None:
            print(val.data,end=" ")
            val = val.next
        print()
        return

node = LinkedList()
node.addEnd(10)
node.addEnd(20)
node.addEnd(30)
node.addEnd(40)
node.printKth(2)
node.print()
print(node.size())