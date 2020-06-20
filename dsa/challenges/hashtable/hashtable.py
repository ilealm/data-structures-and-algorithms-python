from dsa.challenges.linked_list.linked_list import LinkedList
# I need to execute
# PYTHONPATH='.' python dsa/challenges/hashtable/hashtable.py
# to I can execute the code


class Hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hash(self, key):
        '''
        Method that receives a key an generates a number based on the key, which
        never can be greater than self.size
        Always is going to return the same value for the same key.
        '''
        hashed_value = 0

        for ch in key:
            hashed_value += ord(ch)

        hashed_value *= 41
        hashed_value = hashed_value % self.size

        return hashed_value


    def add(self, key, value):
        if not key or not value:
            raise Exception ('The key and values must be valid.')
            return

        print('-----------')
        print(key)
        # obtain the position on the table for this key
        index = self.hash(key)

        # if self.table == None means I need to create a linkedlist and added to this position
        if not self.table[index]:
            self.table[index] = LinkedList()

        self.table[index].insert([key, value])

        self.table[index].display()





if __name__ == "__main__":
    # ll = LinkedList()
    # ll.insert('iris')
    # print('here')
    # print(ll)
    myHT = Hashtable(5)

    key='iris'
    myHT.add(key, key + ' value')
    key='siri'
    myHT.add(key, key + ' value')
    key='ian'
    myHT.add(key, key + ' value')

    print(myHT.table[4].display())

#  $ PYTHONPATH='.' python package_a/module_a_a.py
# export PYTHONPATH=~/codefellows/401/data-structures-and-algorithms-python/dsa/

# PYTHONPATH='.' python dsa/challenges/hashtable/hashtable.py
# this works and executes, but only when I run this
