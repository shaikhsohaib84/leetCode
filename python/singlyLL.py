import copy
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SLinkedList:
    def __init__(self):
        self.headval = None
    
    def insert_node_start(self, value):
        new_node = Node(value)
        new_node.next = self.headval
        self.headval = new_node
    
    def insert_node_last(self, value):
        new_node = Node(value)
        last = self.headval
        if not last:
            self.headval = new_node
            return
        while last.next:
            last = last.next
        last.next = new_node

    def insert_node_between(self, old_value, new_value):
        new_node = Node(new_value)
        curr_node = self.headval
        if not curr_node:
            self.headval = new_node
            return
        while curr_node.data != old_value:
            curr_node = curr_node.next
        if curr_node.data == old_value:
            new_node.next = curr_node.next
            curr_node.next = new_node
            return
        print('not found')
    
    def del_node_start(self):
        head = self.headval


    def listNode(self):
        head = self.headval
        while head is not None:
            print(head.data)
            head = head.next

n1 = SLinkedList()
n1.insert_node_start('Monday')
n1.insert_node_last('Tuesday')
n1.insert_node_start('Monday_101')
n1.insert_node_between('Tuesday1', 'Friday')
n1.insert_node_last('Wednesday')

n1.listNode()