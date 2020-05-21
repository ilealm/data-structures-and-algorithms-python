from challenges.linked_list.linked_list import LinkedList, Node

def merge_list(list_a, list_b):

    current_a = list_a.head
    current_b = list_b.head

    while current_a and current_b:
        # save cursors
        temp_a = current_a.next
        temp_b = current_b.next

        # make the zip
        current_a.next = current_b
        current_b.next = temp_a

        # move to new cursors
        current_a = temp_a
        current_b = temp_b

    return list_a.head



# if __name__ == "__main__":
#     ll_a = LinkedList()
    # ll_a.append('A')
    # ll_a.append('B')
    # ll_a.append('C')
    # ll_b = LinkedList()
    # ll_b.append('1')
    # ll_b.append('2')
    # ll_b.append('3')

    # print(ll_a)
    # print(ll_b)
    # print(merge_list(ll_a, ll_b))
