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



# def fun_name(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# var=eval(input("enter any dict :"))      # ye error case h imp h 
# fun_name(var) 



# def fun_name(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# var=eval(input("enter any dict :"))      # ye error case h imp h 
# fun_name(**var) 

# def fun_name(**n):
#     for k,v in n.items():
#         print(f'{k}={v}')
# var=eval(input("enter any dict :"))      # ye error case h imp h 
# fun_name(**var) 

# =================================================== types of function =======================================
# 1.  with argument and with return 

# def show_datails(name):
#     return name 
# x=input("enter your name:")
# result = show_datails(x)
# print (result)

# # 2. with argument and without return 
# def show_datails(name):
#     print(name) 
# x=input("enter your name:")
# show_datails(x)

# #3. without argument and with return

# def show_datails():
#     return x 
# x=input("enter your name:")
# result = show_datails()
# print (result)


#4. without argument without return 
# def show_datails():
#    x=input("enter your name:")
#    print(x)

# show_datails()

#******************************************  variable scope  ****************************************

# x,y=11,22
# def add():
#     print(x+y)
# add()    


#******************************************** global scope  ******************************************************

# x,y=11,33
# def add():
#     p,q=22,55    # local 
#     print(p,q)
#     print(x,y)   #global

# add()
# print(x,y)
# print(p,q)



# x,y=10,22
# def add():
#     x=20
#     print(x)
# add()   
# print(x) 

# # afer ham local variable ko global bnaana ho to global keyword ka use kr skte hh 
# x,y=10,22
# def add():
#     global z
#     z=20
#     print(z)
# add()   
# print(z) 

# ager dono same nme se defind ho to local value  nikalne ke liye
# x=10
# def add():
#     x=20
#     print(globals()['x'])
# add()  


#  sum krne ke liye
# x=10
# def add():
#     x=20
#     sum = globals()['x'] + x
#     print(sum)
# add()    