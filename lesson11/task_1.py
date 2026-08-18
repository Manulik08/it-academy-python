print("Задание 1")
def power_factory(power: int):
    def power_factory_number(x: int | float):
        return x ** power
    return power_factory_number

num_square = power_factory(2)
num_cube = power_factory(3)

print(num_square(5))
print(num_cube(2))
print(num_square(8))
print(num_cube(3))


