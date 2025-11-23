#!/usr/bin/python3
def best_score(a_dictionary):
    if str(type(a_dictionary)) == str(type(None)):
        return None
    else:
        a = []
        for i in sorted(a_dictionary):
            a += [a_dictionary[i]]
        for i in a_dictionary:
            if a_dictionary[i] == max(a):
                return i
