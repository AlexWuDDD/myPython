def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = round((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def binary_search_recursion(list, item):
    mid_index = len(list)//2
    if len(list) == 0:
        return None
    if item > list[mid_index]:
        return binary_search_recursion(list[mid_index+1:], item)
    elif item < list[mid_index]:
        return binary_search_recursion(list[:mid_index], item)
    else:
        return mid_index


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
print(binary_search_recursion(my_list, 0))
print(binary_search_recursion(my_list, -1))
