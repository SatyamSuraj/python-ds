class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_array(self):
        arr = []
        if self.head is None:
            return arr
        node = self.head
        while node:
            arr.append(node.data)
            node = node.next_node
        return arr

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f"{ str(node.data)} -> "
            node = node.next_node  
        
        ll_string += "None"
        print(ll_string)

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            node = Node(data, self.head)
            self.head = node

    def insert_end(self, data):
        if self.head is None:
            self.insert_beginning(data)

        self.last_node.next_node = Node(data)
        self.last_node = self.last_node.next_node
        
ll = LinkedList()
