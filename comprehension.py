x = [1, 2, 3, 4]

'''
y = []
for item in x:
    y.append(item * item)
'''
# comprehension - LIST
# new_list = [expression1 FOR variable IN old_list IF expression2]
y = [item * item for item in x if item > 2]
print(y)

# comprehension - DICT
# new_dict = {expression1:expression2 for variable in list if expression3}
z = {item: item * item for item in x}
print(z)

# Generator expressions:
# The advantage of using a generator expression is that the entire list isn’t generated in 
# memory, so arbitrarily large sequences can be generated with little memory overhead.
g = (item * item for item in x)
for item in g:
    print(item)
