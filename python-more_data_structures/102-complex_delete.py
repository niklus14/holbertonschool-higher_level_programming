#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    deletes keys with a specific value in a dictionary.
    """
    # 1st. create a snapshot of the keys to iterate over safely.
    # We use list() to make a copy of the keys.
    # If we looped through a_dictionary directly, Python would crash
    # as soon as we deleted the first item.
    keys_to_check = list(a_dictionary.keys())

    # 2nd. loop through our snapshot list
    for key in keys_to_check:

        # 3rd. check the value in the REAL dictionary
        if a_dictionary.get(key) == value:
            # 4th. delete the entry from the REAL dictionary
            del a_dictionary[key]

    # 5th. return the modified dictionary
    return a_dictionary
