def as_hex_digit(number: int) -> str:
    if number < 10:
        return str(number)
    match number:
        case 10:
            return "A"
        case 11:
            return "B"
        case 12:
            return "C"
        case 13:
            return "D"
        case 14:
            return "E"
        case 15:
            return "F"


def my_hex_positive(number: int) -> str:  # For positive numbers only
    if number == 0:
        return ""
    return my_hex_positive(number // 16) + as_hex_digit(number % 16)


def my_hex(number: int) -> str:  # For any integer
    if number == 0:
        return str(0)
    if number < 0:
        return "-" + my_hex_positive(-number)
    return my_hex_positive(number)


test_positive = 255
test_negative = -37

print("Number '"+str(test_positive)+"' 16 based:")
print(f"Built in python function 'hex': {hex(test_positive)}")
print(f"My function: {my_hex(test_positive)}")

print()

print("Number '"+str(test_negative)+"' 16 based:")
print(f"Built in python function 'hex': {hex(test_negative)}")
print(f"My function: {my_hex(test_negative)}")

