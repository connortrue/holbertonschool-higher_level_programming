#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the replaced elements
    new_list = []

    # Iterate over each element in my_list
    for element in my_list:
        # Check if the current element is equal to the search element
        if element == search:
            # If it is, append the replace element to the new list
            new_list.append(replace)
        else:
            # If it is not, append the current element to the new list
            new_list.append(element)

    # Return the new list
    return new_list
