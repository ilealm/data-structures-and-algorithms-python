
# this class will behave as my node in the queue
class Animal:
    def __init__(self, kind, next_ = None):
        self.kind = kind
        self.next = next_


    def __str__(self):
        return f'I am an Animal object of the type {self.kind}.'



class AnimalShelter():
    def __init__(self):
        self.front = None
        self.rear = None

    def __repr__(self):
        return f"The rear is {self.rear} and the front is {self.front}"

    def __str__(self):
        return f"The rear is {self.rear} and the front is {self.front}"


    def enqueue(self, kind):
        new_node = Animal(kind)

        #is the 1st element
        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = self.rear.next



    def dequeue(self, pref=None):
        if (pref != 'Cat') and (pref != 'Dog'):
            return None

        if not self.is_empty():
            temp_node = self.front
            self.front = self.front.next
            temp_node.next = None

            # if there are no more nodes, clear rear
            if self.front == None : self.rear = None

            return temp_node.kind
        else:
            raise Exception ("Can't dequeue in an empty Queue.")


    def peek(self):
        if not self.is_empty():
            return self.front.kind
        else:
            raise Exception ("Can't peek in an empty Queue.")


    def is_empty(self):
        return self.front == None





