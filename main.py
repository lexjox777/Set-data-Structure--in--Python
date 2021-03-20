# Set item are enclosed in curly brackets {}

# Set is unordered

# Set is mutable

# Set element are unique

# Set can contain only immutable items

'''
Python Set Attributes
'''
# print(dir(set))




'''
Creating Python Set
'''
# set is curly brackets {} but set cant be written like Set={} ,this makes it a class of dict...Empty set can be written in set=set() Thus
# set = set ()
# print(type(set))

# set ={1,2,3}
# print(set)


# '''
# Modifying a set in Python
# '''
# set_example={'hello','world!'}
# # print(set_example)
# set_example.add('yay!')
# set_example.add(('hey'))
# set_example.update([1,2,3])
# print(set_example)


# print(help(set_example))


'''
Removing elements from a set
'''

# set_example={1,2,3,4}

# set_example.discard(1)
# set_example.remove(2)
# set_example.pop()
# print(set_example)

# set does not allow duplicate Thus
# print({'hello','world','hello','hello'})

# '''
# Set Union Operations
# '''

# a= {1,2,3,6,7}
# b={4,5,6,7,8,9}
# print(a | b)
# # the above can be written same way below
# print(a.union(b))
#------------------
'''
Set Intersection Operations
'''

# a= {1,2,3,6,7}
# b={4,5,6,7,8,9}
# print(a & b)
# print(a.intersection(b))

'''
Set Difference Operations
'''
# a= {1,2,3,6,7}
# b={4,5,6,7,8,9}
# print(a - b)
# print(a.difference(b))
# print(b-a)
# print(b.difference(a))

'''
Set Symmetric difference
'''

a= {1,2,3,6,7}
b={4,5,6,7,8,9}
print(a ^ b)
print(a.symmetric_difference(b))

'''
Set Method
'''
print(dir(set))