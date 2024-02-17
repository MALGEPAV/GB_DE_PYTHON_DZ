def duplicated_elements(some_list: list) -> list:
    unique_elements = set(some_list)
    value_counts = [(element, some_list.count(element)) for element in unique_elements]
    return [element for (element, count) in value_counts if count > 1]


my_list = [1, 2, 3, 2, 1]
print(duplicated_elements(my_list))
