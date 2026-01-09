collection1 = [False, False, False]
collection2 = (False, True, False)
collection3 = {True, True, True}

print(any(collection1))
print(any(collection2))
print(any(collection3))
print(any(['0']))

print(all(collection1)) # not all truthy