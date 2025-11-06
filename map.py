# #====================================  map()  =============================================
# # collection of array


# # syntax :-

# # collection (d,f,t,e)

# # def fun_name():
# #     fun_body
# # list(map(fun_name, collection))    


# #q.1.================================================================

# # l=[1,2,3,4,5]

# # def squar(n):
# #     return n*n
# # result=map(squar,l)
# # print (result)
# # print(list(result))



# #  map(fun_name , collection1 , collection2,collection3)
# # l1=[11,22,33,44]
# # l2=[1,2,3]
# # l3=[1,2,3,4,5,6,7]

# # def add(x,y,z):
# #     return x+y+z
# # result = list(map(add , l1,l2,l3))
# # print(result)

# #*************************************************** filter() ********************************************************
# #syntax========>>>>>>>>>>>>

# # collection/iterator

# # def fun_name(x):
# #     fun_body
# # result = filter(fun_name , collection/itretor)    

# #q1.>

# # l=[1,2,3,4,5,6,7]
# # def even(n):
# #     if n%2==0:
# #         return n
# # result=filter(even,l)
# # print(result)
# # print(list(result))

# # #==================== even oddd==========================================
# # l=[1,2,3,4,5,6,7]
# # def evenodd(n):
# #     if n%2==0:
# #         return even
# #     else:
# #         return'odd'
# # result=filter(evenodd,l)
# # print(result)
# # print(list(result))

# # map in even odd  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# # l=[1,2,3,4,5,6,7]
# # def evenodd(n):
# #     if n%2==0:
# #         return evenodd
# #     else:
# #         return'odd'
# # result=list(map(evenodd,l))
# # print(result)
# # print(list(result))


# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ reduce  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# #syntax>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # import functools

# # collection/iterator

# # def fun_name(x,y):
# #     function body
# # result = functools.reduce(fun_nmae,iterator,initial value)

# # que. 1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import functools
# l=[1,2,3,4,5,6,7]
# def add(x,y):
#     return x+y
# result = functools.reduce(add,l)
# print(result)
  


# #((((((((((((((((((((((((((((((((((((((((((((     max      ))))))))))))))))))))))))))))))))))))))))))))
# import functools
# l=[10,2,30,46,50,6,7]
# def max(x,y):
#     if x>y:
#         return x
#     else:
#         return y
 
# result = functools.reduce(max,l)
# print(result)


# #((((((((((((((((((((((((((((((((((((((((((((((((((((((((     min      ))))))))))))))))))))))))))))))))))))))))))))))))))))))))


# import functools
# l=[10,2,30,46,50,6,76]
# def min(x,y):
#     if x<y:
#         return x
#     else:
#         return y
 
# result = functools.reduce(min,l)
# print(result)



# # //////////////////////////////////////////////// lambda() /////////////////////////////////////////////
# p=lambda x,y:print(x+y) 
# # p(4,5)
# # print(p(3,4))
# z=p(4,5)
# print(z)
# print(z)
# print(z) 

# l=[1,2,3,4,5,6,7,8]
# print(list(filter(lambda n: n if n%2==0 else None,l)))

# import functools
# l=[1,2,3,4,5]
# print(functools.reduce(lambda x,y: x if x>y else y,l))
# print(functools.reduce(lambda x,y: x if x<y else y,l)


#////////////////////////////////////////  decorator  =//////////////////////////////////////////////



# def outer_fun(main_fun):
#     return inner_fun  
#     def inner_fun(parameters):
#         main_fun()
  
    



# def outer(x):
#     def inner():
#             print("welcome")
#             x()
#     return inner
# def display()  :
#         print("hello")   
# res=outer(display)    
# res()




# def outer(x):
#     def inner(p,q):
#           p=p+5
#           q=q+9
#           x(p,q)
#     return inner
# @outer
# def display (x,y):
#       print(x+y)
# display(1,2)      
# 
# def decorator(x):
#     def inner (p,q,r):
#         p=p-5
#         q=q-10
#         r=r-15
#         z=x(p,q,r)
#         return z
#     return inner
# @decorator
# def add (a,b,c):
#     return a-b-c
# res=add(2,4,6)
# print(10,20,30)

def decorator(x):
    def inner(p,q,r):
        p=p+5
        q=q+10
        r=r+5
        return p+q+r
    return inner
@decorator
def add (a,b,c):
    return a+b+c
res=add(20,40,10)
print(res)

# //////////////////////////////////////////////////////generator////////////////////////////////////////////////////////////