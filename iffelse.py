


# /////////////////////////////////////////////////// conditional statement ////////////////////////////////////////////////////

# x= eval (input("enter any value"))
# if isinstance (x,object):
#     print ('user gives python objects')

# x= int (input ("enter any number:"))
# if (x%2==0):
#     print("give vale is evel")
#     print("Thanks for visit")

# x=int(input("enter any value"))
# if x%2==0:
#     print("given value is positive")
#     print("not a even negative")
#     print("thank for checking")

    #================================================= if - elif  statement ==============================================================#
    #  1)   if  === (independ , may - be )
    #  1)  if- elif  === (independ , may - be )
    #  1)   if-elif-else  === (depended , may - be )
 
#      syntax :---
#     if   (condition 1):
       
#        | statement 1

#    elif (cndition 2) :
   
#       |  statements 2

#  elif (cndition 3) :
   
#       |  statements 3
#              |
#              |
      
#       conditions==============================

# n = int(input ('enter any value '))
# if n>0:
#     print(f'given value{n} is positive')

#     elif n==0 :
#     print(f'given value{n} is zero')

#     elif n<0:
#     print( f'given value{n} is nagetive')

#///////////////////////////////////////////////////  if - elif - else  ////////////////////////////////////////////////////////////////////
#( to check more then one conditio)

# n = int(input ('enter any value'))
# if n>0 and n<=10:
#     print(f'given values {n} lier in b/w 0-10 ')

# elif n>10 and n<=20:
#     print(f'given values {n} lier in b/w 11-20 ')

# elif n>20 and n<=30:
#     print(f'given values {n} lier in b/w 21-30 ')

# else : print(f'given value{n}not valid for check condition')

# year = int(input ('enter a year'))
# if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
#     print (f'{year} is leap year')
    
# else:
#     print(f'{year} is not leap year')

# print(0.1+0.2==0.3)*************************************** interview questions*********************************************************

#/////////////////////////////////////////////////////////  iterative  statement  ////////////////////////////////////////////////////////////////
# to avoide repation of same block of code we use iteractive looping statements 

# while loop   (infinite iterations)
# for loop   (finite iterations)

####  while condition ###
# while - body executed when condition is true
# n=int(input("enter any number:"))
# i=1
# while (i<=n):
#       print(i)
#       i=i+1

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ isme numbers hirizantale me print hoge but comma last wale numbers me bhi show hoga ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# i=1
# while (i<=n):
#       print(i,end=",")
#       i=i+1

# #^^^^^^^^^^^^^^^^^^^^^^^ isme numbers hirizantale show hoga with comma(,)///////////////////////////////////////

# while (i<=n):
#       if i<=(n-1):
#         print(i,end=",")
#       else:
#          print(i)
#       i=i+1

#////////////////////////// isme sum ho rha h numbers ka /////////////////////////////////

# i,sum=1,0
# while (i<=n):
#       sum=sum+i
#       if i<=(n-1):
#         print(i,end="+")
#       else:
#          print(i,end="=")
#       i=i+1
# print(sum)


#//////////////////////////////////////////////////////// while loop///////////////////////////////////////////////////////////

# n=5
# i=1
# while i<=n:
#     print('*'*n)
#     i=i+1

# n=1
# i=1
# while i<=n:
#     print(' '(n-i)+''*i)
#     i=i+1


# i=5
# while i<=n:
#     print(' '(n-i)+''*i)
#     i-0

# 



# n=5
# i=0
# while i<n:
#     # print('*'*(n-i)+''*i)
#     print(''*i+'*'*(n-i))
#     i=i+1555555


# while i<n:
#     # print('*'*(n-i)+''*i)
#     print(''*i+'*'*(n-i))
#     i=i+1



# n=5
# i=1
# while i<n:
   
#     print('*-'*i+' '*(n-i))
#     i=i+1
#     print(i)

# i=i-2
# while i>=1:
#         print('*-'*i + ' '*(n-i))
#         i=i-1


# n=5
# i=0
# while i<n:
#     print(''*i+'*' *(n-i))
#     i=i+1

# i=i-2
# while i>=0:
#     print('*'*(n-i)+''*i)
#     i=i-1




    #///////////////////////////////////////// amarstrong numbers /////////////////////////////////////

# n = int(input("enter any number "))
# x=n
# tg=0
# while n>0:
#         tg=tg+1
#         # n=n//10=0
#         n= n//10
# print(tg,n)
# print(f'total_digit of {x}  is {tg}')



n = int(input("enter any number "))
x=n
q=p=n
sum=0
tg=0
while n>0:
        tg=tg+1
        n=n//10
while   p>0 :
        last_digit=x%10
        sum = sum+last_digit**tg
        p=p//10
if q==sum:
        print("Armstrong" )             
else:
    
        print("Armstrong" ) 