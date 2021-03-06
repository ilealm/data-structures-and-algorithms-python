from collections import deque

class Node:
    def __init__(self, value, left = None,  rigth = None):
        self.value = value
        self.left = left
        self.right = rigth

    def __str__(self):
        return f"Node: {self.value}"

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

    # added
    def BreadthFirst(self,tree):
        list_return = []

        # if not tree.root : return 'The Tree is empty.'
        if not tree.root : return list_return

        breadth = Queue()

        breadth.enqueue(tree.root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            list_return.append(front.value)

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

        return list_return

    # added Jun 3rd, Challenge 18
    def FindMaximumValue(self):
        if self.root == None : return None

        current_max_value = self.root.value

        def traverse(current_node):
            nonlocal current_max_value
            if not current_node : return

            if current_node.value > current_max_value:
                current_max_value = current_node.value

            traverse(current_node.left)
            traverse(current_node.right)

        traverse(self.root)


        return current_max_value

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

# added
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


# python dsa/challenges/tree/tree.py
# if __name__ == "__main__":
#     tree = BinarySearchTree()
    # tree.add(100)
    # tree.add(50)
    # tree.add(1200)
    # tree.add(20)
    # tree.add(700)
    # tree.add(90)
    # tree.add(150)
# #     tree2 = tre
# #     print(tree.BreadthFirst(tree2))
    # print(tree.FindMaximumValue())




