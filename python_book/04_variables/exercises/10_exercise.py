# if obj = 42, which statements reassign and which mutate the variable?

# obj = 'ABcd' reassigning from 42 to 'ABcd'
# obj.upper() mutating 'ABcd' to 'ABCD' - neither
# obj = obj.lower() reassigning obj from 'ABCD' to 'abcd'
# print(len(obj)) neither, performing a function referencing the variable obj
# obj = list(obj) reassigning obj to ['a', 'b', 'c', 'd']
# obj.pop() mutating the obj list to become ['a', 'b', 'c']
# obj[2] = 'X' mutating the obj list to ['a', 'b', 'X']
# obj.sort() mutating the list again to ['X', 'a', 'b'] since capital characters come before lowercase.
# set(obj) mutate the list into a set
# obj = tuple(obj) reassign obj to a tuple - neither