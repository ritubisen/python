 # relation b/w paramiters and arguments ---------
#1.  position argument--------
# def fun_name(x,y,z):
#     print(f'{x,y,z}')
# p=int(input("enter any value:"))
# q=int(input("enter any value:"))
# r=int(input("enter any value:"))
# fun_name(p,q,r,22)

# #2.  default argument------------***************--------------

# def fun_name(x=0 , y=0 , z=0):
#     print(f'{x,y ,z}')

# fun_name()
# fun_name(10)
# fun_name(20,10)
# fun_name(10,20,30)

#3.  variable lenght positional argument---------------------

# syntax=============  def fun_name(*args):
#                      print (args)
#                      print (type(args))
# fun_name(variable_lenght argument)


# def fun_name(*args):
#     print(args)
#     print(type(args))

# t=eval(input("enter any tuple"))
# fun_name(t)


# fun_name()
# fun_name(10,20,30,40,50.60,70)


# def add_all(*n):
#     sum=0
#     for i in n :
#         sum=sum + i
#     print(f'sum is{sum}')

# add_all(10,20,30,40)

# def add_all(*n):
#     sum =0
#     for i in n:
#         print(i)
#         for j in i:
#             sum= sum+j
#     print(f'sum is {sum}')  
# var =eval(input("enter any collection :"))
# add_all(var)


# def add_all(*n):
#     print(n)

# var =eval(input("enter any collection :"))
# add_all(*var)    



# def add_all(*n):
#  sum=0
#  for i in n:
#     sum = sum +i
#  print(f'sum is {sum}')        #  ye unpacking ka logic hai isse sum nikal skte hai 

# var =eval(input("enter any collection :"))
# add_all(*var)    


#  some casese of error ============================

# def display(x=0,y):
#     print(f'x,y')
# display(10,20) 



# def display(*n , x):
#     print(f'{n,x}')
# display(10,20,30)  
    

# def display( x , y=0,*z):
#     print(f'{x,y,z}')
# display(10,20,30,40,50)  
    

# 4.  keyword argument --------------------------------------------------*************************************--------------------------

def fun_name(x,y,z):
    print(f'{x,y,z}')
fun_name(x=10,y=88,z=66)   