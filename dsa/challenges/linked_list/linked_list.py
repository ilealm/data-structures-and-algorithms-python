class LinkedList():
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"The head is {self.head}"

    def insert(self, value):
        new_node = Node(value)
        if self.head : new_node.next = self.head
        self.head = new_node

    def includes(self,value):
        current = self.head
        while current:
            if current.value == value : return True
            current = current.next
        return False

    def __str__(self):
        str = ""
        current = self.head

        while current:
            str += "{ " + current.value + " } -> "
            current = current.next

        return str + "NULL"

class Node():
    def __init__ (self, value, next_ = None):
        self.value =  value
        self.next = next_

        if (not next_ == None) and ( not isinstance(next_, Node)):
            raise TypeError("The value of the next node MUST be a node")


    def __repr__(self):
        return f"{self.value} -> {self.next}"





