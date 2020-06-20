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

        # if the head is none, then call insert function
        if not current :
            self.insert(value)
            return

        while current.next:
            current = current.next
        current.next = new_node


    def insert_before(self, value, new_val):
        new_node = Node(new_val)
        current = self.head

        if not current: return

        if current.value == value :
            new_node.next = self.head
            self.head = new_node
            return

        while current.next:
            if current.next.value == value:
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

    def how_many_nodes(self):
        current = self.head
        num_nodes = 0

        while current:
            num_nodes += 1
            current = current.next

        return num_nodes

    def kth_from_end(self, k_value):
        ll_num_nodes = (self.how_many_nodes())
        nodes_to_traverse = ll_num_nodes - k_value

        if k_value < 0 : return "The value to search must be greater than 0."
        if 0 > nodes_to_traverse : return "The kth position is greater than the Linkedlist lenght."

        current = self.head
        for i in range(0, nodes_to_traverse):
            current = current.next

        return current.value


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


    ### methods added to use hastables
    # this one is from Ahmad
    def display(self):
        '''
        Display the values of the linked list
        '''
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values

    def add_to_hashtable(self, value):
        '''
        This function works for adding to hash tables.
        Since hashtales can't have duplicates keys, we need to search for the key, if it exist, the value of that key
        will be changed. If the key doesn't exist in the list, will be added to the list.
        '''
        print('in add_to_hashtable.. ', value[0])
        current = self.head
        print(ll.head)
        while current:
            if current.value == value : return True
            current = current.next
        return False

    def get_hashtable_value(self, key):
        '''
        value = [key, value]
        Method that traverse the linked list to check for a key (position 0) and returns its value (position 1)
        if the key is not found, returns False
        '''

        current = self.head
        while current:
            if current.value[0] == key : return current.value[1]
            current = current.next
        return False

class Node():
    def __init__ (self, value, next_ = None):
        self.value =  value
        self.next = next_

        if (not next_ == None) and ( not isinstance(next_, Node)):
            raise TypeError("The value of the next node MUST be a node")


    def __repr__(self):
        return f"{self.value} -> {self.next}"



# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append("one")
#     ll.insert("one")
#     ll.insert("two")
#     ll.insert("tree")
#     ll.insert("four")
#     ll.insert("five")
#     ll.insert("six")
# if append when list is null, call insert
    # print(ll)
    # print('total nodes', ll.how_many_nodes())
    # pos = 0 to validate
    # pos = 3
    # print('the value of position:', pos, ' is:', ll.kth_from_end(pos))
# kth_from_end

