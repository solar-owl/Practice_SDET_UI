import numpy as np

def get_sorted_descending_and_ascending(values):
    sorted_values = sorted(values)
    sorted_values_reverse = sorted(values, reverse=True)
    return sorted_values, sorted_values_reverse

def get_names_for_delete(names):
    names_dict = {name: len(name) for name in names}
    values = list(names_dict.values())
    average = np.mean(values)
    min_difference = min(abs(values - average))
    del_names = []
    for key, value in names_dict.items():
        if abs(value - average) == min_difference:
            del_names.append(key)
    return del_names

def get_names_after_delete(first_names, del_names):
    return list(filter(lambda x: x not in del_names, first_names))