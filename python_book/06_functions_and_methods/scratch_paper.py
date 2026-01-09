# def well_howdy(who):
#     greeting = 'Howdy'
#     print(f'{greeting}, {who}')

# well_howdy('Angie')
# print(greeting) # name error name not defined

# greeting = 'Hi' #assign

# def well_howdy(who):
#     greeting = 'Howdy' # assign
#     print(f'{greeting}, {who}') # variable shadowing - 'Howdy'

# well_howdy('Anders')
# print(greeting) # 'Hi'

# greeting = 'Salutations' # global scope

# def well_howdy(who):
#     print(f'{greeting}, {who}')

# well_howdy('Angie')
# print(greeting)

def scope_test():
    if True:
        foo ='Hello'
    else:
        bar = 'Goodbye'

    print(foo) # 'Hello'
    print(bar) # name error

scope_test() # UnboundLocalError: cannot access local variable 'bar' where it is not associated with a value

