# LIST --------------------------------------


# l=[10,20,'python','java']
# print(l)
# print(type(l))
# print(id(l))


# TuPLE--------------------------------

# t=[10,20,'python',30,'java']
# print(t)
# print(type(t))
# print(id(t))


#DICTIONARY--------------------

# d={
#     'name':'ritu',
#     'age': 20,
#     'city':'bhopal'
# }
# print(d)
# print(type(d))
# print(id(d))


#SET=========================------------

# S={10,20,30,50,'PYTHON','JAVA','ritu','bisen',30,70,50,45,77,88,99,}
# print(S)
# print(type(S))
# print(id(S))


#frozenset---------------------------------------

d={
    'name':'ritu',
    'age':20,
    'city':'bhopal',

}
fs=frozenset(d)
print(fs)
print(type(fs))
print(id(fs))


# LITERAL TYPES================================
# 1. NUMERIC  -->>>> DIGIT
# 2. STRING   -->>>> '-' , "-" , '''-'''
# 3. LIST     -->>>> []
# 4. TUPLE    -->>>> ()
# 5. DICTIONARY  -->>>> {'KEY': 'VALUE'}
# 6. SET      -->>>>  {}
# 7. FROZENSET  -->>>> FROZENSET(COLLECTION)