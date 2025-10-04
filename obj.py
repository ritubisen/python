# # object in pyton----------------------------------

# #numeric

# #1. integer  -->  int() -->  0--------------------
# x=int()
# print(x)
# print(type(x))

# #2. float --> float() --> 0.0 ------------------------
# x=float
# print(x)
# print(type(x))

# #3. complex  --> complex()  --> oj------------------------
# x=complex
# print(x)
# print(type(x))

# list --> list() --> []
# string --> str() --> 
# tuple --> tuple()  -->()
# dict --> dict()  --> {}
# ----------------------------------------------empty declaration-----------------------------------
# set  --> set()  -->  set()
# frozenset  --> frozenset()  --> frozenset()
# ---------------------------------------------------type casting--------------------------------------------

# x= int (input("enter any num")) 
# print(x)
# print(type(x))

# x=eval(input("enter anything"))
# print(x)
# print(type(x))

#========================== in-built function===================


# l=[22,44,66,77,55,]

# print(max(l))
# print(min(l))
# print(len(l))
# print(sum(l))

#=======================  in - built class  =========================================




# print("hello")
# print("hii")
# x=20
# y=40
# print(x,y , sep=',')
# print("hello" , end=',')
# print("hii")


#======================================== python object ===================================================================#

# . mutable
# 1. list
# 2. dictinory
# 3. set

# # . immutable
# 1. numeric
# 2. tuple   --  collection of elements   == 1 . 
# 3. string
# 4. frozenset
# 5. boolean

# x=10
# y=10
# print(id(x),id(y))


# a='python'
# b='java'
# print(id(a),id(b))


# c=[99,44,66,88]
# d=[66,88,44,99]
# print(id(c),id(d))


# p=(99,44,66,88)
# s=(66,88,44,99)
# print(id(p),id(s))

# //========================== tuple ==================================//

# t=(10,20,"python",[1,2,3,4,4],(1,2,3,4))
# t=10,

# print(t)
# print(type(t))

# x='python'
# y='python'
x={'x':10 , 'y':10}
y={'x':10 , 'y':10}
print(id(x),id(y))