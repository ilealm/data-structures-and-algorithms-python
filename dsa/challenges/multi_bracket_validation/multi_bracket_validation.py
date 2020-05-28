class Node():
    def __init__(self, value, next_ = None):
        self.value =  value
        self.next = next_

        if (not next_== None) and (not isinstance(next_, Node)):
            raise TypeError("Error creating the node. The value of next must be a node.")

    def __repr__(self):
        return f"{self.value} -> {self.next}"


class Stack():
    def __init__(self):
        self.top = None

    def __repr__(self):
        return f"The top is {self.top}"

    def __str__(self):
        return f"The top is {self.top}"

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            temp_node = self.top
            self.top = self.top.next
            temp_node.next = None
            return temp_node.value
        else:
            raise Exception ("Can't pop from an empty stack.")


    def peek(self):
        if not self.is_empty():
            return self.top.value
        else:
            raise Exception ("Can't peek on an empty stack.")
            # return  #do I need to use return or exption will end code execution??

    def is_empty(self):
        return self.top == None

class Validator:
    def __init__(self):
        self.stack = Stack()

    def is_opening_bracket(self, char):
        if char in ['(','[','{']:
            return True
        else:
            return False

    def is_closing_bracket(self, char):
        if char in [')',']','}']:
            return True
        else:
            return False

    def is_match_on_stack(self, closing_bracket):
        # TODO: when is only 1 ele in stack
        # if the char is the closing bracket match for the top of the stack, then is correct, else return false
        if self.stack.is_empty() : return False

        opening_bracket = self.stack.pop()
        print('revewing ', opening_bracket, 'and ', closing_bracket)
        if opening_bracket == '(' :
            if closing_bracket == ')' :
                print('valid () pair')
                return True
            else:
                return False

        if opening_bracket == '[' :
            if closing_bracket == ']' :
                print('valid () pair')
                return True
            else:
                return False

        if opening_bracket == '{' :
            if closing_bracket == '}' :
                print('valid {} pair')
                return True
            else:
                return False


    def multi_bracket_validation(self, word):
        valid_string = True
        bracket_mismatch = False
        for ch in range(len(word)) :
            if self.is_opening_bracket(word[ch]) :
                self.stack.push(word[ch])
                # print('just pushed ', self.stack.peek())

            if self.is_closing_bracket(word[ch]) :
                # print('reviewing closign', word[ch])
                # valid_string = self.is_match_on_stack(word[ch])
                if not self.is_match_on_stack(word[ch]) : valid_string = False

        return valid_string


if __name__ == "__main__":
    val = Validator()
    word = 'Iris'
    # word = 'iris'
    print(word)
    print('Valid string: ', val.multi_bracket_validation(word))
    # print(val)
