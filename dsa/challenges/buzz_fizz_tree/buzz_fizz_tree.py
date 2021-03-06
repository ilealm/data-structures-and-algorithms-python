from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node: {self.value}"


class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.appendleft(value)

    def dequeue(self):
        if not self.is_empty():
            return self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0




class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if not self.root : return 'The root is empty.'

        return f'The root is {self.root.value}'

    def preOrder(self):
        list_return = []

        if self.root == None : return list_return

        def traverse(current_node):
            if not current_node : return

            list_return.append(current_node.value)
            traverse(current_node.left)
            traverse(current_node.right)

        traverse(self.root)

        return list_return

    def inOrder(self):
        list_return = []

        if self.root == None : return list_return

        def traverse(current_node):
            if not current_node : return

            traverse(current_node.left)
            list_return.append(current_node.value)
            traverse(current_node.right)


        traverse(self.root)
        return list_return

    def postOrder(self):
        list_return = []

        if not self.root :  return list_return

        def traverse(current_node):
            if not current_node : return

            traverse(current_node.left)
            traverse(current_node.right)
            list_return.append(current_node.value)

        traverse(self.root)
        return list_return

    def FizzBuzzTree(self,tree):

        def getFizzBuzzValue(value):
            if (value % 3 == 0) and (value % 5 == 0):
                return 'FizzBuzz'
            elif (value % 5) == 0 :
                return 'Buzz'
            elif (value % 3) == 0:
                return 'Fizz'
            else:
                return str(value)



        if not tree : return 'The Tree is empty.'


        breadth = Queue()
        # create a copy of the tree
        return_tree = tree

        breadth.enqueue(return_tree.root)


        while not breadth.is_empty():
            front = breadth.dequeue()
            # change the value of the node, using getFizzBuzzValue
            front.value = getFizzBuzzValue(front.value)

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

        return return_tree

    # adds to breadt first
    def BreadthFirstAdd(self, value):
        new_node = Node(value)
        breadth = Queue()

        if not self.root : self.root = new_node

        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()

            if not front.left:
                front.left = new_node
                return
            elif not front.right:
                front.right = new_node
                return

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)







class BinarySearchTree(BinaryTree):
    def __str__(self):
        if not self.root : return 'The root is empty.'

        return f'The root is {self.root.value}'


    def add(self, value):
        new_node = Node(value)

        if self.root == None :
            self.root = new_node
            return

        def traverse(current_node, new_node):

            if not current_node : return

            if new_node.value < current_node.value:
                if current_node.left == None :
                    current_node.left = new_node
                else:
                    traverse(current_node.left, new_node)
            else:
                if current_node.right == None :
                    current_node.right = new_node
                else:
                    traverse(current_node.right, new_node)


        traverse(self.root, new_node)


    def contains(self, value):
        if not self.root: return False

        def traverse(current_node, value_to_search):
            if not current_node : return False
            if current_node.value == value_to_search :
                return True
            else:
                if value_to_search < current_node.value :
                    return traverse(current_node.left, value_to_search)
                else:
                    return traverse(current_node.right, value_to_search)

        return traverse(self.root, value)

