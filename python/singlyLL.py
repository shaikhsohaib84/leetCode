class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SLinkedList:
    def __init__(self):
        self.headval = None
    
    def listNode(self):
        head = self.headval
        while head is not None:
            print(head.data)
            head = head.next
    
    def addNodeAtLast(self, data):
        head = self.headval
        if head is None:
            self.headval = Node(data)
        else:
            head.next = Node(data)
    
    def addNodeAtStart(self, data):
        head = self.headval
        if head is None:
            self.headval = Node(data)
        else:
            # new_node = Node(data)
            # new_node.next = self.headval.next
            # self.headval.next = new_node

            new_node = Node(data)
            new_node.next = self.headval
            self.headval= new_node

            



n1 = SLinkedList()

n1.headval = Node('mon')
n2 = Node('Tue')
n3 = Node('Wed')

n1.headval.next = n2
n2.next = n3

# n1.listNode()
n1.addNodeAtLast('Thur')
# n1.listNode()

n1.addNodeAtStart('Fri')
n1.listNode()