my_list= [1,-1,1,2,2,3,4,4,4,4,-4,5]
your_list=[1,4,5,6,6,6,9]
my_set={4,8,7,3}
your_set={1,3,2}
our_set={1}
#1
def union_of_sets(set1, set2):
    return set1.union(set2)
print(union_of_sets(my_set,your_set))
#2
def intersection_of_sets(set1, set2):
    return set1.intersection(set2)
print(intersection_of_sets(my_set,your_set))
#3
def difference_of_sets(set1, set2):
    return set1.difference(set2)
print(difference_of_sets(my_set, your_set))
#4
def is_subset(set1, set2):
    return set1.issubset(set2)
print(is_subset(our_set, your_set))
#5
def check_element(set1, element):
    return element in set1
print(check_element(my_set,7))
#6
def set_length(my_set1):
    return len(my_set1)
print(set_length(my_set))
#7
def list_to_set(my_list):
    return set(my_list)
print(list_to_set(my_list))
#8
def remove_element(my_set1, element):
    my_set1.discard(element)
    return my_set
print(remove_element(my_set,7))
#9
def clear_set(my_set):
    my_set.clear()
    return my_set
print(clear_set(our_set))
#10
def is_set_empty(my_set1):
    return not my_set1
print(is_set_empty(my_set))
#11
def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)
print(symmetric_difference(my_set, your_set))
#12
def add_element(my_set1, element):
    my_set1.add(element)
    return my_set1
print(add_element(my_set,7))
#13
def pop_element(my_set1):
    return my_set1.pop()
print(pop_element(my_set))
print(my_set)
#14
def find_maximum(my_set1):
    return max(my_set1)
print(find_maximum(my_set))
#15
def find_minimum(my_set1):
    return min(my_set1)
print(find_minimum(my_set))
#16
def filter_even_numbers(my_set1):
    return {x for x in my_set1 if x % 2 == 0}
print(filter_even_numbers(my_set))
#17
def filter_odd_numbers(my_set1):
    return {x for x in my_set1 if x % 2 != 0}
print(filter_odd_numbers(my_set))
#18
def create_set_of_range(start, end):
    return set(range(start, end + 1))
print(create_set_of_range(2,9))
#19
def merge_and_deduplicate(list1, list2):
    return set(list1) | set(list2)
print(merge_and_deduplicate(my_list, your_list))
#20
def check_disjoint_sets(set1, set2):
    return set1.isdisjoint(set2)
print(check_disjoint_sets(my_set, your_set))
#21
def remove_duplicates(input_list):
    return set(list(input_list))
print(remove_duplicates(my_list))
#22
def count_unique_elements(input_list):
    return len(set(input_list))
print(count_unique_elements(my_list))
#23
import random
def generate_random_set(start, end, size):
    return set(random.sample(range(start, end + 1), size))
print(generate_random_set(2, 20, 6))
