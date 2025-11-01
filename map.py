#====================================  map()  =============================================
# collection of array


# syntax :-

# collection (d,f,t,e)

# def fun_name():
#     fun_body
# list(map(fun_name, collection))    


#q.1.================================================================

# l=[1,2,3,4,5]

# def squar(n):
#     return n*n
# result=map(squar,l)
# print (result)
# print(list(result))



#  map(fun_name , collection1 , collection2,collection3)
# l1=[11,22,33,44]
# l2=[1,2,3]
# l3=[1,2,3,4,5,6,7]

# def add(x,y,z):
#     return x+y+z
# result = list(map(add , l1,l2,l3))
# print(result)

#*************************************************** filter() ********************************************************
#syntax========>>>>>>>>>>>>

# collection/iterator

# def fun_name(x):
#     fun_body
# result = filter(fun_name , collection/itretor)    

#q1.>

# l=[1,2,3,4,5,6,7]
# def even(n):
#     if n%2==0:
#         return n
# result=filter(even,l)
# print(result)
# print(list(result))

# #==================== even oddd==========================================
# l=[1,2,3,4,5,6,7]
# def evenodd(n):
#     if n%2==0:
#         return even
#     else:
#         return'odd'
# result=filter(evenodd,l)
# print(result)
# print(list(result))

# map in even odd  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# l=[1,2,3,4,5,6,7]
# def evenodd(n):
#     if n%2==0:
#         return evenodd
#     else:
#         return'odd'
# result=list(map(evenodd,l))
# print(result)
# print(list(result))


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ reduce  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#syntax>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import functools

# collection/iterator

# def fun_name(x,y):
#     function body
# result = functools.reduce(fun_nmae,iterator,initial value)

# que. 1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import functools
l=[1,2,3,4,5,6,7]
def add(x,y):
    return x+y
result = functools.reduce(add,l)
print(result)
  


#((((((((((((((((((((((((((((((((((((((((((((     max      ))))))))))))))))))))))))))))))))))))))))))))
import functools
l=[10,2,30,46,50,6,7]
def max(x,y):
    if x>y:
        return x
    else:
        return y
 
result = functools.reduce(max,l)
print(result)


#((((((((((((((((((((((((((((((((((((((((((((((((((((((((     min      ))))))))))))))))))))))))))))))))))))))))))))))))))))))))


import functools
l=[10,2,30,46,50,6,76]
def min(x,y):
    if x<y:
        return x
    else:
        return y
 
result = functools.reduce(min,l)
print(result)
