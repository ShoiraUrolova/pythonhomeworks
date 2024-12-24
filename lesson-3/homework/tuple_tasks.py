#1
my_list= [1,-1,1,2,2,3,4,4,4,4,-4,5,]
my_tuple = (1,2,2,3,3,3,4,4,4,4)
your_tuple= (5,6,5)
our_tuple=()
def count_occurrences(tpl, element):
    return tpl.count(element)
print(count_occurrences(my_tuple,4))
#2
def max_element(tpl):
    if not tpl:
        return None
    return max(tpl)
print(max_element(my_tuple))
#3
def min_element(tpl):
    if not tpl:
        return None  # Handle empty tuple
    return min(tpl)
print(min_element(my_tuple))
#4
def check_element(tpl, element):
    return element in tpl
print(check_element(my_tuple,5))
#5
def first_element(tpl):
    if tpl:
        return tpl[0]
    return None
print(first_element(my_tuple))
#6
def last_element(tpl):
    if tpl:
        return tpl[-1]
    return None
print(last_element(my_tuple))
#7
def tuple_length(tpl):
    return len(tpl)
print(tuple_length(my_tuple))
#8
def slice_tuple(tpl):
    return tpl[:3]
print(slice_tuple(my_tuple))
#9
def concatenate_tuples(tpl1, tpl2):
    return tpl1 + tpl2
print(concatenate_tuples(my_tuple, your_tuple))
#10
def is_empty(tpl):
    return len(tpl) == 0
print(is_empty(our_tuple))
#11
def find_all_indices(tpl, element):
    return [index for index, value in enumerate(tpl) if value == element]
print(find_all_indices(your_tuple,5))
#12
def second_largest(tpl):
    if len(tpl) < 2:
        return None  
    sorted_tpl = sorted(tpl)
    return sorted_tpl[-2]
print(second_largest(my_tuple))
#13
def second_smallest(tpl):
    if len(tpl) < 2:
        return None 
    sorted_tpl = sorted(tpl)
    return sorted_tpl[1]
print(second_smallest(my_tuple))
#14
def single_element_tuple(element):
    return (element,)
print(single_element_tuple(8))
#15
def list_to_tuple(lst):
    return tuple(lst)
print(list_to_tuple(my_list))
#16
def is_sorted(tpl):
    return tpl == tuple(sorted(tpl))
print(is_sorted(your_tuple))
#17
def max_of_subtuple(tpl, start, end):
    subtuple = tpl[start:end+1]
    return max(subtuple)
print(max_of_subtuple(my_tuple,0,5))
#18
def min_of_subtuple(tpl, start, end):
    subtuple = tpl[start:end+1]
    return min(subtuple)
print(min_of_subtuple(my_tuple,4,8))
#19
def remove_element_by_value(tpl, value):
    temp_list = list(tpl)
    if value in temp_list:
        temp_list.remove(value)
    return tuple(temp_list)
print(remove_element_by_value(my_tuple,2))
#20
def create_nested_tuple(tpl, subtuple_size):
    return tuple(tuple(tpl[i:i+subtuple_size]) for i in range(0, len(tpl), subtuple_size))
print(create_nested_tuple(my_tuple, 4))
#21
def repeat_elements(tpl, times):
    return tuple(element for element in tpl for _ in range(times))
print(repeat_elements(my_tuple,2))
#22
def create_range_tuple(start, end):
    return tuple(range(start, end+1))
print(create_range_tuple(2,6))
#23
def reverse_tuple(tpl):
    return tpl[::-1]
print(reverse_tuple(my_tuple))
#24
def is_palindrome(tpl):
    return tpl == tpl[::-1]
print(is_palindrome(your_tuple))
#25
def unique_elements(tpl):
    seen = set()
    return tuple(x for x in tpl if not (x in seen or seen.add(x)))
print(unique_elements(my_tuple))