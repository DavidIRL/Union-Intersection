class Node:
    def __init__(self, value):
        # Creating double-linked list for easy appending
        self.value = value
        self.prev = None
        self.next = None


    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0


    def __str__(self):
        current = self.head
        output = []

        while current:
            output.append(str(current.value))
            current = current.next
        return "->".join(output)


    def append(self, value):
        if value is None:
            raise ValueError('Node value cannot be empty')
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.num_elements = 1
        
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.num_elements += 1
        

    def size(self):
        return self.num_elements

