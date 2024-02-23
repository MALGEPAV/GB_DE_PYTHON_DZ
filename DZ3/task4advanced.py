def plus_one(already_packed: list, overall_weight: int,
             left_unpacked: dict, weight_capacity: int) -> list:
    plus_one_lists = list()
    extended = False
    for thing in left_unpacked:
        if overall_weight + left_unpacked[thing] <= weight_capacity:
            new_left_unpacked = left_unpacked.copy()
            plus_one_lists.extend(plus_one([*already_packed, thing],
                                           overall_weight + new_left_unpacked.pop(thing),
                                           new_left_unpacked,
                                           weight_capacity))
            extended = True
    if not extended:
        plus_one_lists = [already_packed]
    return plus_one_lists


def packing_options(things_with_weights: dict, weight_capacity: int) -> list:
    ordered_options = plus_one([], 0, things_with_weights, weight_capacity)
    options = set(["|".join(sorted(ordered_option)) for ordered_option in ordered_options])
    options = list(map(lambda string: string.split("|"), options))
    return options


dict_of_things = {"book": 500, "tooth brush": 30, "spoon": 50, "tent": 3000, "cup": 100,
                  "rope": 1000, "canned food": 300, "matches": 20, "phone": 200, "knife": 300}
capacity = 1000

print("All possible packing options:")
for opt in packing_options(dict_of_things, capacity):
    print(opt, f"weight: {sum([dict_of_things[key] for key in opt])}")
