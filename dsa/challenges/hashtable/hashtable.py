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



        print(self.table[index].display())



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


if __name__ == "__main__":
    myHT = Hashtable(5)

    key='iris'
    myHT.add(key, key + ' value')
    key='siri'
    myHT.add(key, key + ' value')
    key='iris'
    myHT.add(key, key + ' upd value')
    # key='emma'
    # myHT.add(key, key + ' value')

    key='ian'
    myHT.add(key, key + ' value')
    key='ian'
    myHT.add(key, key + ' upd value')

    # key='emma'
    # print(myHT.get(key))
    # key='siri'
    # print(myHT.get(key))
    # key='iris'
    # print(myHT.get(key))

    # key='nobody'
    # print(myHT.get(key))

    # key='nobody'
    # key='erich'
    # print(myHT.contains(key))
    # key='iris'
    # print(myHT.contains(key))

    # key='ian'
    # myHT.add(key, key + ' value')

    # print(myHT.table[4].display())

