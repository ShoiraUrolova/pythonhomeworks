#1
my_dictionary= {'a':1,'b':2, 'c':-3, 'd':3, 'c':4}
your_dictionary= {'c':3, 'd':4, 'e':5, 'f':6}
our_dictionary= {'g': 10}
def get_value(input_dict, key, default=None):
    return input_dict.get(key, default)
print(get_value(my_dictionary,'d', 'Not Found'))
#2
def check_key(input_dict, key):
    return key in input_dict
print(check_key(my_dictionary,'b'))
#3
def count_keys(input_dict):
    return len(input_dict)
print(count_keys(my_dictionary))
#4
def get_all_keys(input_dict):
    return list(input_dict.keys())
print(get_all_keys(my_dictionary))
#5
def get_all_values(input_dict):
    return list(input_dict.values())
print(get_all_values(my_dictionary))
#6
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Create a copy of dict1
    merged_dict.update(dict2)   # Update with dict2's items
    return merged_dict
print(merge_dictionaries(my_dictionary, your_dictionary))
#7
def remove_key(input_dict, key):
    return input_dict.pop(key, None) 
print(remove_key(my_dictionary, 'c'))
#8
def clear_dictionary(input_dict):
    input_dict.clear()
print(clear_dictionary(our_dictionary))
#9
def check_empty(input_dict):
    return not bool(input_dict)
print(check_empty(my_dictionary))
#10
def get_key_value_pair(input_dict, key):
    if key in input_dict:
        return key, input_dict[key]
    return None
print(get_key_value_pair(my_dictionary, 'a'))
#11
def update_value(input_dict, key, value):
    input_dict[key] = value
    return input_dict
print(update_value(your_dictionary,'c',2))
#12
def count_value_occurrences(input_dict, value):
    return list(input_dict.values()).count(value)
print(count_value_occurrences(my_dictionary, 2))
#13
def invert_dictionary(input_dict):
    return {v: k for k, v in input_dict.items()}
print(invert_dictionary(my_dictionary))
#14
def find_keys_with_value(input_dict, value):
    return [key for key, val in input_dict.items() if val == value]
print(find_keys_with_value(my_dictionary, 3))
#15
def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))
keys=['a', 'b','c']
values=[4, 5, 9]
print(create_dict_from_lists(keys, values))
#16
def check_nested_dict(input_dict):
    return any(isinstance(val, dict) for val in input_dict.values())
print(check_nested_dict(my_dictionary))
#17
def get_nested_value(input_dict, *keys):
    for key in keys:
        input_dict = input_dict.get(key, {})
    return input_dict
input_dict=  {'a': {'b': {'c': 1}}}
print(get_nested_value(input_dict, *keys))
#18
#19
def count_unique_values(input_dict):
    return len(set(input_dict.values()))
my_dict= {'a':1, 'c':2, 'd':2, 'e':3}
print(count_unique_values(my_dict))
#20
def sort_dict_by_key(input_dict):
    return dict(sorted(input_dict.items()))
print(sort_dict_by_key(my_dict))
#21
def sort_dict_by_value(input_dict):
    return dict(sorted(input_dict.items(), key=lambda item: item[1]))
print(sort_dict_by_value(my_dict))
#22
def filter_by_value(input_dict, condition):
    return {k: v for k, v in input_dict.items() if condition(v)}
print(filter_by_value(my_dictionary, lambda x: x>0))
#23
def have_common_keys(dict1, dict2):
    return not dict1.keys().isdisjoint(dict2.keys())
print(have_common_keys(my_dictionary, your_dictionary))
#24
def create_dict_from_tuple(tuple_of_pairs):
    return dict(tuple_of_pairs)
tuple_of_pairs= (('a', 1), ('b', 2), ('c', 3))
print(create_dict_from_tuple(tuple_of_pairs))
#25
def get_first_key_value_pair(input_dict):
    return next(iter(input_dict.items()), None)
print(get_first_key_value_pair(my_dict))