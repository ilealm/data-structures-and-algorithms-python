class Stack():
    def __init__(self):
        self.top = None

    def __repr__(self):
        return f"The top is {self.top}"

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node

    def pop(self):
        if self.top == None:
            raise Exception ("Can't pop from an empty stack.")
            return

        if not self.is_empty():
            temp_node = self.top
            self.top = self.top.next
            temp_node.next = None
            return temp_node.value

    def peek(self):
        if self.top == None:
            raise Exception ("Can't peek on an empty stack.")
            return

        if not self.is_empty():
            return self.top.value

    def is_empty(self):
        return self.top == None





class Node():
    def __init__(self, value, next_ = None):
        self.value =  value
        self.next = next_

        if (not next_== None) and (not isinstance(next_, Node)):
            raise TypeError("Error creating the node. The value of next must be a node.")

    def __repr__(self):
        return f"{self.value} -> {self.next}"

    # def __str__(self):
    #     return f"{self.value} -> {self.next}"



# mynode = Node("Red")
# print(mynode)
