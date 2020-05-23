class Stack():
    def __init__(self):
        self.top = None

    def __repr__(self):
        return f"The top is {self.top}"

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node

    def pop(self):
        # TODO: add is_empty
        if self.top == None:
            raise Exception ("Can not pop from an empty stack.")
            return

        temp_node = self.top
        self.top = self.top.next
        # remove the relationship to the stack
        temp_node.next = None
        return temp_node.value

    def peek(self):
        # TODO: add is_empty
        if self.top == None:
            raise Exception ("Can't peek on an empty stack.")
            return

        return self.top.value




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
