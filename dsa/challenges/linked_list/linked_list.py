class LinkedList():
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"The head is {self.head}"

    def insert(self, value):
        new_node = Node(value)
        if self.head : new_node.next = self.head
        self.head = new_node

    def append(self,value):
        new_node = Node(value)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    def insert_before(self, value, new_val):
        new_node = Node(new_val)
        current = self.head

        if not current: return

        # # if there is only the head node, append to the right
        # if not current.next and current.value == value :
        if current.value == value :
            new_node.next = self.head
            self.head = new_node
            return

        while current.next:
            if current.next.value == value:
                print('here')
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next


    def insert_after(self, value, new_val):
        new_node = Node(new_val)
        current = self.head

        if not current: return

        while current:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next


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



# ll = LinkedList()
# ll.insert("First")
# # ll.insert("Second")
# # ll.insert("Third")
# # ll.append('Fourth')
# ll.insert_before("First", '1.4')
# print(ll)

# ll = LinkedList()
# ll.insert("First")
# ll.insert("Second")
# print('original', ll.__str__())
# ll.insert_before("Second", "1.5")
# actual = ll.__str__()
# expected = "{ 1.5 } -> { Second } -> { First } -> NULL"
# print ("actual", actual)
# print ("expeed", expected)
