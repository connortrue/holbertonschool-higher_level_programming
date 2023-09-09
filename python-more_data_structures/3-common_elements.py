#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_elements_set = set()
    for elem in set_1:
        if elem in set_2:
            common_elements_set.add(elem)
    return common_elements_set
