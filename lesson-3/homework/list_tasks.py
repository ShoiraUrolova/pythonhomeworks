#1
def count_occurrences(lst, element):
    return lst.count(element)
my_list= [1,-1,1,2,2,3,4,4,4,4,-4,5,]
your_list=[]
our_list=[6,7]
print(count_occurrences(my_list, 4))
#2
def sum_of_elements(lst):
    return sum(lst)
print(sum_of_elements(my_list))
#3
def max_element(lst):
    return max(lst) if lst else None
print(max_element(my_list))
#4
def min_element(lst):
    return min(lst)
print(min_element)
#5
def check_element(lst, element):
    return element in lst
print(check_element(my_list,5))
#6
def first_element(lst):
    return lst[0] if lst else None
print(first_element(my_list))
#7
def last_element(lst):
    return lst[-1] if lst else None
print(last_element(my_list))
#8
def slice_list(lst):
    return lst[:3]
print(slice_list(my_list))
#9
def reverse_list(lst):
    return lst[::-1]
print(reverse_list(my_list))
#10
def sort_list(lst):
    return sorted(lst)
print(sort_list(my_list))
#11
def remove_duplicates(lst):
    return list(set(lst))
print(reverse_list(my_list))
#12
def insert_element(lst, index, element):
    lst.insert(index, element)
    return lst
print(insert_element(my_list, 0, 3))
#13
my_list.index(5)
print(my_list.index(1,0))
#14
def is_list_empty(lst):
    return len(lst) == 0
print (is_list_empty(your_list))
#15
def count_even_numbers(lst):
    return sum(1 for x in lst if x % 2 == 0)
print(count_even_numbers(my_list))
#16
def count_odd_numbers(lst):
    return sum(1 for x in lst if x % 2 != 0)
print(count_odd_numbers(my_list))
#17
def concatenate_lists(lst1, lst2):
    return lst1 + lst2
print(concatenate_lists(my_list, your_list))
#18
def find_sublist(lst, sublst):
    sublen = len(sublst)
    return any(sublst == lst[i:i + sublen] for i in range(len(lst) - sublen + 1))
print(find_sublist(my_list, our_list))
#19
def replace_element(lst, old_element, new_element):
    try:
        index = lst.index(old_element)
        lst[index] = new_element
    except ValueError:
        pass  # Element not found; do nothing
    return lst
print(replace_element(my_list,3,1))
#20
def second_largest(lst):
    unique_lst = list(set(lst))
    if len(unique_lst) < 2:
        return None
    unique_lst.sort()
    return unique_lst[-2]
print(second_largest(my_list))
#21
def second_smallest(lst):
    unique_lst = list(set(lst))
    if len(unique_lst) < 2:
        return None
    unique_lst.sort()
    return unique_lst[1]
print(second_smallest(my_list))
#22
def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]
print(filter_even_numbers(my_list))
#23
def filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]
print(filter_odd_numbers(my_list))
#24
def list_length(lst):
    return len(lst)
print(list_length(my_list))
#25
def crate_copy(lst):
    return lst.copy()
print(crate_copy(my_list))
#26
def get_middle_element(lst):
    n = len(lst)
    if n == 0:
        return None
    elif n % 2 == 1:
        return lst[n // 2]
    else:
        return lst[n // 2 - 1:n // 2 + 1]
print(get_middle_element(our_list))
#27
def max_of_sublist(lst, start, end):
    if start < 0 or end > len(lst) or start >= end:
        raise ValueError("Invalid start or end indices.")
    sublist = lst[start:end]
    return max(sublist)
print(max_of_sublist(my_list,1,8))
#28
def min_of_sublist(lst, start, end):
    if start< 0 or end > len(lst) or start>= end:
        raise ValueError("Invalid start or end indicies.")
    sublist = lst[start:end]
    return min(sublist)
print(min_of_sublist(my_list, 1,8))
#29
def remove_element_by_index(lst, index):
    if index < 0 or index >= len(lst):
        raise IndexError("Index out of range.")
    del lst[index]
    return lst
print(remove_element_by_index(my_list,1))
#30
def is_sorted(lst):
    return lst == sorted(lst)
print(is_sorted(my_list))
#31
def repeat_elements(lst, times):
    return [item for item in lst for _ in range(times)]
print(repeat_elements(my_list,2))
#32
def merge_and_sort(lst1, lst2):
    merged_list = lst1 + lst2
    return sorted(merged_list)
print(merge_and_sort(my_list, your_list))
#33
def find_all_indices(lst, element):
    return [index for index, value in enumerate(lst) if value == element]
print(find_all_indices(my_list,1))
#34
def rotate_list(lst, k):
    if not lst:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]
print(rotate_list(my_list,2))
#35
def create_range_list(start, end):
    return list(range(start, end + 1))
print(create_range_list(1, 3))
#36
def sum_of_positive_numbers(lst):
    return sum([num for num in lst if num > 0])
print(sum_of_positive_numbers(my_list))
#37
def sum_of_negative_numbers(lst):
    return sum([num for num in lst if num < 0])
print(sum_of_negative_numbers(my_list))
#38
def is_palindrome(lst):
    return lst == lst[::-1]
print(is_palindrome(my_list))
#39
def create_nested_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
print(create_nested_list(my_list,2))
#40
def unique_elements_in_order(lst):
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list
print(unique_elements_in_order(my_list))


