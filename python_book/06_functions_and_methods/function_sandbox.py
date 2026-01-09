
numbers = [2, 5, 8, 10, 13]
print(any([number % 2 == 0 for number in numbers])) # True
print(all([number % 2 == 0 for number in numbers])) # False