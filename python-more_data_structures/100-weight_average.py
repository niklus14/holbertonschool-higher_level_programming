#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    returns the weighted average of all integers tuple (<score>, <weight>)
    """
    # 1st. safety check: If the list is empty, return 0 immediately.
    # Using "if not my_list" is the Pythonic way to check for empty lists.
    if not my_list:
        return 0

    total_weighted_score = 0
    total_weight = 0

    # 2nd. loop through each tuple in the list
    for tuple_item in my_list:
        # Unpack the tuple for clarity
        score = tuple_item[0]
        weight = tuple_item[1]

        # 3rd. calculate the numerator (top part of fraction)
        # Multiply score by weight and add to total
        total_weighted_score += (score * weight)

        # 4th. calculate the denominator (bottom part of fraction)
        # Just add the weight to the total weight
        total_weight += weight

    # 5th. perform the final division
    # Python 3 automatically handles float division (e.g., 5 / 2 = 2.5)
    return total_weighted_score / total_weight
