# NOTE: I called the variable a constant, but did not handle it as such on line 10.

# When I run the following code here is what will happen

NAME = 'Victor' # initialize a constant variable called NAME with a value if 'Victor'
# Now we print the following lines where the value of NAME is 'Victor'.
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina' # now we reassign NAME to a value of 'Nina'

# we now print the following three lines where the value of NAME is 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# Output:

# 'Good Morning, Victor'
# 'Good Afternoon, Victor'
# 'Good Evening, Victor'
# 'Good Morning, Nina'
# 'Good Afternoon, Nina'
# 'Good Evening, Nina'