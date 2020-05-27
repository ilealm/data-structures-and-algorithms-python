from dsa.challenges.stacks_and_queues.stacks_and_queues import Stack

# PLEASE EXECUTE ON TERMINAL
# export PYTHONPATH=~/codefellows/401/data-structures-and-algorithms-python/
# so can import from a sibling folder


class PseudoCode():
    def __init__(self):
        self.main_stack = Stack()
        self.moving_stack = Stack()

    def __repr__(self):
        return self.main_stack.__repr__()

    def __str__(self):
        return self.main_stack.__repr__()

    def enqueue(self, value):
        self.main_stack.push(value)

    def dequeue(self):
        if self.main_stack.is_empty():
            raise Exception ("The queue is empty.")
        # step 1 pop all and push to moving_stack (reverse the stack)
        while not self.main_stack.is_empty():
            self.moving_stack.push(self.main_stack.pop())
        # step 2.1 From moving_stack, pop it and save the value.
        return_value = self.moving_stack.pop()
        # step 2.2 Pop everything from moving_stack and enqueue to main_stack
        while not self.moving_stack.is_empty():
            self.main_stack.push(self.moving_stack.pop())
        # step 4 return saved value
        return return_value

# if __name__ == "__main__":
#     pc = PseudoCode()
#     pc.enqueue("one")
#     pc.enqueue("two")
#     pc.enqueue("three")
#     pc.enqueue("four")
#     print(pc)
#     # print(pc.dequeue())
#     # print(pc.dequeue())

#     # print(pc.dequeue())
#     # print(pc.dequeue())
#     print ('modified main stack:', pc)
#     print(pc.__str__())
