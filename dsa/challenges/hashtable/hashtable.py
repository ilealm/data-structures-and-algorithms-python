from dsa.challenges.linked_list.linked_list import LinkedList
# I need to execute
# PYTHONPATH='.' python dsa/challenges/hashtable/hashtable.py
# to I can execute the code
# OR in this directory: PYTHONPATH="../../../" python hashtable.py


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

        # obtain the position on the table for this key
        index = self.hash(key)

        # if self.table == None means I need to create a linkedlist and added to this position
        if not self.table[index]:
            self.table[index] = LinkedList()

        self.table[index].add_to_hash_table(key, value)


    def table_is_empty(self, index):
        '''
        Method that returns boolean depending if self.table[index] == None
        '''
        return  self.table[index] == None


    def get(self, key):
        '''
        Method that returns the value of the key.
        If is null, returns False.
        '''
        if not key :
            raise Exception ('The key and values must be valid.')
            return

        # obtain the position on the table for this key
        index = self.hash(key)

        # validate if the table have a value before calling methods, to avoid errors
        if self.table_is_empty(index) : return False

        return (self.table[index].get_hashtable_value(key))



    def contains(self, key):
        '''
        Method that takes a key and retuns a boolean depending if
        the key exist in the table.
        '''
        if not key :
            raise Exception ('The key and values must be valid.')
            return


        index = self.hash(key)

        if self.table_is_empty(index) : return False

        return (self.table[index].key_exist_in_hashtable(key))


    def display_hashtable(self):
        for index in range(0, self.size):
            text = ""
            text += "\t" + str(index) + "\t"
            if not self.table[index]:
                text += "----"
            else:
                ll = self.table[index].display()
                for node in ll:
                    text += "[" + str(node[0]) + ' => ' + str(node[1]) + "]"
            print(text)


