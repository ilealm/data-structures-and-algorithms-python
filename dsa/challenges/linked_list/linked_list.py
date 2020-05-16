class LinkedList():
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"The head is {self.head}"

    def insert(self, value):
        new_node = Node(value)
        if self.head : new_node.next = self.head
        self.head = new_node


class Node():
    def __init__ (self, value, next_ = None):
        self.value =  value
        self.next = next_

    def __repr__(self):
        return f"{self.value} -> {self.next}"

if __name__ == "__main__":
    ll = LinkedList()
    print("head", ll.head)

    ll.insert("One")
    print("head", ll.head)
    # one = Node("One")
    # two = Node("Two")
    # print("original values: head:", myHead, ' : ', one, two)

    # myHead.head = one
    # one.next = two

    # print("new values head ", myHead)
    # print("new values one:",one)
    # print("new values two:", two)





