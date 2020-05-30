class Node:
    def __init__(self, value, left = None,  rigth = None):
        self.value = value
        self.left = left
        self.right = rigth

class BinaryTree:
    def __init__(self):
        self.root = None

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


class BinarySearchTree(BinaryTree):
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


    def contains(self, value):

        exists_in_tree = False



        return exists_in_tree


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(100)
    bst.add(50)
    bst.add(120)
    bst.add(25)
    bst.add(75)
    bst.add(110)
    # print ('                     ',bst.root.value)
    # print ('              ', bst.root.left.value, ' ---  ', bst.root.right.value)

    print(bst.preOrder())
    print(bst.inOrder())
    print(bst.postOrder())

