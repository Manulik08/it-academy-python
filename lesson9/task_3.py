print("Задание 3")
def convert(value: int | float, from_unit: str, to_unit: str):
    if from_unit == "km":
        if to_unit == "m":
            value *= 1000
        else:
            value *= 100000

    if from_unit == "m":
        if to_unit == "km":
            value /= 1000
        else:
            value *= 100

    if from_unit == "cm":
        if to_unit == "m":
            value /= 100
        else:
            value /= 100000

    return value

print(convert(5, "km", "m"))