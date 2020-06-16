def insertion(list_to_review):
    for index in range(1, len(list_to_review)):
        position = index
        temp_value = list_to_review[index]

        while position > 0 and list_to_review[position - 1] > temp_value:
            list_to_review[position] = list_to_review[position-1]
            position = position -1

        list_to_review[position] = temp_value

    return list_to_review
