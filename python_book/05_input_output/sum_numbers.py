# number1 = int(input('Enter the first number: ')) # coerce input to a string
# number2 = int(input('Enter the second number: '))

number1 = input('Enter the first number: ') # avoid coercion
number2 = input('Enter the second number: ')

sum = float(number1) + float(number2) # coerce on assignment

print(f'The numbers {number1} and {number2} add to {sum}')