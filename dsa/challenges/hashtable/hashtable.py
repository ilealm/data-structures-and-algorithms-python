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

        # before inserting the new value, will check if the key already exists, if so, I will update the value of that key, so I
        # don't have duplicates.

        # print(self.table[index].includes([key, value]))
        self.table[index].insert([key, value])
        # self.table[index].add_to_hashtable([key, value])

        # print(self.table[index].display())


    def get(self, key):
        '''
        Metod that returns the value of the key.
        If is null, returns False.
        '''
        if not key :
            raise Exception ('The key and values must be valid.')
            return

        # obtain the position on the table for this key
        index = self.hash(key)

        return (self.table[index].get_hashtable_value(key))


if __name__ == "__main__":
    myHT = Hashtable(5)

    key='iris'
    myHT.add(key, key + ' value')
    key='siri'
    myHT.add(key, key + ' value')
    key='emma'
    myHT.add(key, key + ' value')

    key='ian'
    myHT.add(key, key + ' value')


    key='emma'
    print(myHT.get(key))
    key='siri'
    print(myHT.get(key))
    key='iris'
    print(myHT.get(key))

    key='nobody'
    print(myHT.get(key))

    # key='ian'
    # myHT.add(key, key + ' value')

    # print(myHT.table[4].display())

