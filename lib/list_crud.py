def create_an_empty_list():
    return []

def create_a_list():
    return ['a', 'b', 'c', 'd']

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

add_element_to_end_of_list([1, 2, 3, 4], 5)

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

add_element_to_start_of_list([1, 2, 3, 4], 0)

def remove_element_from_end_of_list(l):
    l.pop()
    return l

remove_element_from_end_of_list([1, 2, 3, 4])

def remove_element_from_start_of_list(l):
    del l[0]
    return l

remove_element_from_start_of_list([1,2,3,4])

def retrieve_first_element_from_list(l):
    return l[0]

retrieve_first_element_from_list([1,2,3,4])

def retrieve_element_from_index(l, index):
    return l[index]

retrieve_element_from_index([1,2,3,4], 2)

def retrieve_last_element_from_list(l):
    return l[-1]

retrieve_last_element_from_list([1,2,3,4])
