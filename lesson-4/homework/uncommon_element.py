list1= list(input("enter the elements of the list1: "))
list2= list(input("enter the elements of the list2: "))
def uncommon_elements(list1, list2):
    # Count elements in each list
    count1 = {}
    count2 = {}
    
    for num in list1:
        count1[num] = count1.get(num, 0) + 1
    for num in list2:
        count2[num] = count2.get(num, 0) + 1
    
    # Find uncommon elements
    result = []
    
    for num in count1:
        if num not in count2:
            result.extend([num] * count1[num])
    for num in count2:
        if num not in count1:
            result.extend([num] * count2[num])
    
    return result
print("result:", uncommon_elements(list1, list2))