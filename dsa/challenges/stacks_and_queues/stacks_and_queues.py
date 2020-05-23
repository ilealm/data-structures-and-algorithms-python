# reference for manipulating stacks and queues:
# from collections import deque
# python -i dsa/challenges/stacks_and_queues/stacks_and_queues.py

class Node():
    def __init__(self, value, next_ = None):
        self.value =  value
        self.next = next_

        if (not next_== None) and (not isinstance(next_, Node)):
            raise TypeError("Error creating the node. The value of next must be a node.")

    def __repr__(self):
        return f"{self.value} -> {self.next}"


class Stack():
    def __init__(self):
        self.top = None

    def __repr__(self):
        return f"The top is {self.top}"

    def __str__(self):
        return f"The top is {self.top}"

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            temp_node = self.top
            self.top = self.top.next
            temp_node.next = None
            return temp_node.value
        else:
            raise Exception ("Can't pop from an empty stack.")


    def peek(self):
        if not self.is_empty():
            return self.top.value
        else:
            raise Exception ("Can't peek on an empty stack.")
            # return  #do I need to use return or exption will end code execution??

    def is_empty(self):
        return self.top == None


class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def __repr__(self):
        return f"The rear is {self.rear} and the front is {self.front}"

    def __str__(self):
        return f"The rear is {self.rear} and the front is {self.front}"


    def enqueue(self, value):
        new_node = Node(value)

        #is the 1st element
        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = self.rear.next


    def dequeue(self):
        if not self.is_empty():
            temp_node = self.front
            self.front = self.front.next
            temp_node.next = None

            # if there are no more nodes, clear rear
            if self.front == None : self.rear = None

            return temp_node.value
        else:
            raise Exception ("Can't dequeue in an empty Queue.")

    def peek(self):
        if not self.is_empty():
            return self.front.value
        else:
            raise Exception ("Can't peek in an empty Queue.")


    def is_empty(self):
        return self.front == None


