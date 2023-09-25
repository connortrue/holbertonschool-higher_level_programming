#!/usr/bin/python3
"""Doc"""


import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"
try:
    # Load the list from the file
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, create a new list
    my_list = []

# Add the command line arguments to the list
my_list.extend(sys.argv[1:])
# Save the updated list back to the file
save_to_json_file(my_list, filename)
