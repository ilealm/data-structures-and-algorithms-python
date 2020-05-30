class Node:
    def __init__(self, value, left = None,  rigth = None):
        self.value = value
        self.left = left
        self.right = rigth

class BinaryTree:
    pass

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return f'The root is {self.root}'


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




if __name__ == "__main__":
    bts = BinarySearchTree()
    # print (bts)
    bts.add(100)
    bts.add(120)
    print (bts.root.right.value)
