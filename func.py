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


def fun_name(*args):
    print(args)
    print(type(args))

t=eval(input("enter any tuple"))
fun_name(t)


# fun_name()
# fun_name(10,20,30,40,50.60,70)
