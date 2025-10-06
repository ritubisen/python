# #data types 
# #1. numeric

# x=10
# print(x)
# print(type(x))


# y=22.4
# print(y)
# print(type(y))

# z=22+4j
# print(z)
# print(type(z))

# a=66
# print(len(a))
# print(max(a))
# print(min(a))


#=====python========in-built function=========================

# s='python'
# print(min(s))
# print(max(s))
# print(len(s))
# print(type(s))
# print(id(s))
# print(s)

#========string=========in-built methods=========================

# p='python'
# print(p.lower())
# print(p.upper())
# print(p.swapcase())
# print(p.title())
# print(p.capitalize())
# print(p.center(100,'!'))
# print(p.join())
# print(p.split())

# s1='ritu'
# s2='bisen'

# print(' '.join((s1,s2)))

# 

# print(s.split('s'))
# print(s.split('s',0))
# print(s.split('s',2))

# s='python'
# print(s.isascii())
# print(s.isdigit())
# print(s.isspace())
# print(s.isnumeric())
# print(s.isdecimal())


#orderd data types
# list is collection of homogenious as well as hetrogenous  elements

# l=['python','java','php']
# l2=[10,32,55,44,33]
# print(max(l))
# print(min(l))
# print(max(l2))
# print(min(l2))
# print(sum(l2))
# # print(sum(l))
# print(len(l2))
# print(len(l))
# print(id(l2))
# print(id(l))



# methods of lists

# m=[22,30 ,3,2,88,'java','php' , 'python']
# print(m.copy())     # copy krega
# print(m.append('java'))   #value add krega 

# print(m.extend('java '))    #ye multiple element ko add krta h
# print(m.extend('p')) 
# print(m.insert()) 

# print(m.pop())     #aakhri element ko hatane ke iye

# print(m)

# print(m.index(22))

# t = (1, 2, 3)
# t[0] = 10       

#-=============================================  {  empty  data type }  ===================================================

import sys
x=int()
x=str()
x=float()
x=tuple()
x=list()
x=set()
x=frozenset()
x=dict()
x=complex()
y=sys.getsizeof(x)
print(y)