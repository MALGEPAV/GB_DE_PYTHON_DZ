def things_to_pack(things_with_weights: dict, weight_capacity: int) -> tuple:
    overall_weight = 0
    things_list = []

    while things_with_weights:
        some_thing = list(things_with_weights.keys())[0]
        some_weight = things_with_weights.pop(some_thing)

        if overall_weight + some_weight > weight_capacity:
            continue

        overall_weight += some_weight
        things_list.append(some_thing)
        
    return things_list, overall_weight


dict_of_things = {"book": 500, "tooth brush": 50, "spoon": 50, "tent": 5000, "cup": 100}
max_weight = 800

list_of_things, weight = things_to_pack(dict_of_things, max_weight)

print("One of the possible lists of things to pack:")
print(list_of_things)
print(f"Overall weight: {weight}")
