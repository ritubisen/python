#*******************************************(((((((((((((((((((((((((((((((((((((    OOPS    )))))))))))))))))))))))))))))))))))))*************************************

  # 1.   class ==========  design of an object
                 
  # 
  # 2.   object             


# #class==>>>>>>>>> 
# class classname :
#     "doc string "
#     variables (properties)
           
#            instance variable
#            class/static variable
#            local variable
    

#     methods (action/behavior)
      
#          constructor
#    -->  instance method 
#     --> class  metod
#     --> static method


# class mee address nikalna hai

# class student:
#       pass

# print(id(student))
# obj1=student
# print (id(obj1))
# obj2=student
# print(id(obj2))

# obekct ke sath 

# class student:
#       school = 'SHSS'
#       def showdeatil():
#             print("wlvomto schil")

# print(dir(student))
# print(student.__doc__)

# parenthencess ki help se constructoer ko call krta hh 
# adresss alag alag aayega
# class student:
#       pass
# obj1=student ()
# obj2=student ()
# obj3=student ()

# print(id(student))
# print (id(obj1),id(obj2),id(obj3))
# ***********************************************(((((((   constructor   )))))))***********************************************
# ek naya object create krte hi constructor change ho jata h hame call krne ki jrurrat nhi hoti h 

# class student:
#       def __init__(self):
#          print("consyructor called")
# obj=student()     
 
      
# class student:
#       def __init__(self,name,quali):
#             self.n=name
#             self.q=quali
# obj1=student('ritu','bca')            
# obj2=student('ritu','bca')   
# print(obj1.n)         
# print(obj2.q)         


# ********************************((((((((((((((((((((((  topics ))))))))))))))))))))))***************************************
# 1.  class 
# 2.  object 
# 3.  constructor 
# 4.  self
# 5.  variable


# ************************************(((((((((((((((((((((    variable    )))))))))))))))))))))********************************

# 1.  instance variable  (object dependout variable)
# 2.  class variable
# 3.  local variable


# class student:
#       def __init__(self,name , rollno)
#             self . n=name
#             self .r  =rollno
# obj1=student('ritu','bca')            
# obj2=student('ritu','bca')   
# print(obj1.n)         
# print(obj2.q) 


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>           decalaration of instance variable              :::::::::::::---------

# 1.  inside class  -<< inside constructor
#                 |
#                   -<< inside instance method
                

# 2.  outside class
        
# class student :
#        def __init__(self,name,rollno):                                  #  inside
#            self.n,self.r=name,rollno               # decalartion
#       def addnew(self,contact):
#            self.c=contact                        # decalration

# obj = student('ritu' , 111)                                            # outside
# x=eval(input("enter contact detail :"))     
# obj.addnew(x)                                        # decalaration
# obj.city='bhopal'
        


#*******************************(((((((((((((((((((((  constructor ke anadar oinstance varible ko likh sakteh )))))))))))))))))))))**************



# class student :
#       def __init__(self,name,rollno):                                  #  inside
#           self.n,self.r=name,rollno               # decalartion
#           print(self.n,self.r)                    #  calling
#       def addnew(self,contact):
#           self.c=contact                            # decalration
#           print(self.n,self.r,self.c,self.city)      # calling                 

# obj = student('ritu' , 111)                                            # outside
# x=eval(input("enter contact detail :"))     
                                       
# obj.city='bhopal'
# obj.addnew(x)                                       # decalaration
# print(obj.n,obj.r,obj.c)                            # calling



# 2.      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>          class varible      (object independent variable )          :::::::::::::------------------------



# class student :                                         
#       school_name='cybrom'                          # decalartion
#       def __init__(self,name,rollno):                                 
#           self.n,self.r=name,rollno               # decalartion
#           student.gread = '10th'
#           print(student.school_name,student.school_city)     # calling
#       def addnew(self):
#           student.principle="python"
#           print(student. school_city,student.gread)           # calling

# student.school_city="bhopal"                      #  declaration 
# obj=student('ritu',987)  
# obj.addnew()  
# print(obj.principle)                             # calling(not recomnded)   
# print(student.principle)                          # calling (recomded)      



# 3. >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>( local variable )>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# class student :
#      def __init__(self):
#           x=10
#           print(x)
#      def new(self):
#           y=10
#           print(y) 
#           # print(x) 
# obj=student()      
# obj.new()       
          

 #  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< """""""""""""""""" methods """"""""""""""""""""""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
 # 
#  # 1.          instance method (first perametar is self) -->>  refer to object 
#    2.            class  method (first parametar is cls)| , @classmethod
#                                                        |--->>> refer to class
#   3.           static method                                                  



# class Book :
#     price=100
#     def __init__(self ,title,total_page):
#          self.t=title
#          self.tp=total_page
#     @classmethod
#     def update_price(cls,p):
#                   cls.p=11
# obj=Book('python',400)  
# print(obj.t,obj.tp,Book.price)  
# x=float(input("enter updated price"))   
# obj.update_price(x)
# obj1=Book('python',500) 
# print(obj.t,obj.tp,Book.price)                


# --------------------------------------------------------------  static method ----------------------------------------------------------------

# class web:
#         def __init__(self,name):
#                 self.n=name
#         @staticmethod        
#         def great():
#                 print("welcome to my web page")    # ststic method h ye
# obj = web('ecomm') 
# obj.great() 



# class web:
#         def __init__(self,name):
#                 self.n=name
#         def great():
#                 print("welcome to my web page")                   
# obj = web
# obj.great() 
# 
# 
# 
# 
# 
# 
# 
# #   --------------------- class  method h isme class variable bn skte h --------------------------------
# class student:
#     school='SHSS'
#     gread='10th'
#     def __init__(self,name,rollno):
#         self.n=name
#         self.r=rollno
#     @classmethod
#     def upgread_grd(cls,new_gread):
#         cls.gread=new_gread 

# print(id(student)) 
# obj1=student('rit',222) 
# obj2=student('ruchi',250)  
# obj3=student('ruchi',250)  
# obj4=student('ruchi',250) 
# print(obj1.gread,obj2.gread) 
# print(obj3.gread,obj4.gread)     
# obj1.upgread_grd('11th')
# print(id(student)) 

# obj5=student('rit',222) 
# obj6=student('ruchi',250)  
# obj7=student('ruchi',250)  
# obj8=student('ruchi',250) 
# print(obj5.gread,obj6.gread) 
# print(obj7.gread,obj8.gread)  
# print(obj1.gread,obj2.gread) 
# print(obj3.gread,obj4.gread)  
                     


#*****************************(((((((((((((((((((((((((((     proparties     )))))))))))))))))))))))))))****************************************

# 1.  abstraction
# 2.  encapsulation
# 3.  inheritance
# 4.  polymorphism

# ----------------------------------------------------------------  inheritance  ----------------------------------------------------------
#----------------------------------------------------------------( parent-child  relation )------------------------------------------------

# single - level 

# class parent:
#     car='toyota'
#     def home(self):
#         print("home from parent")
# class child(parent):
    
#     pass
# obj=child()
# print(obj.car)
# obj.home()

# use super() key


# class parent:
#     car='toyota'
#     def home(self):
#         print("home for parent")
# class child(parent) :
#    def home(self):
#         print("home for child")  
#         super().home() 
# obj=child()
# obj.home()            

#****************************************************  (  multi-lavel  inheritance )  *********************************************************
# class Grandparent:
#     car='bmw'
#     def home(self):
#         print("home for grandparent")
# class Parent(Grandparent)       :
#     def home(self):
#         print("home for parent")
#         super().home()
        
# class Child(Parent) :
#     def home(self):
#        print("home for child")  
#        super().home()        
# obj=Child()     
# obj.home() 


#***************************************************  ( multiple inheritance )  *********************************************************

 #             MRO   (method resulution order  (depth first algorithm per work krta h))........................



# class Parent2:
   
#     def home(self):
#         print("home for parent2")
# class Parent1(Parent2)       :
#     def home(self):
#         print("home for parent1")
#         super().home()
        
# class Child(Parent1,Parent2) :
#     def home(self):
#        print("home for child")  
#        super().home()        
# obj=Child()     
# obj.home() 


# class A:
#     def home(self):
#         print("parent1")
#         B.home(self)
#         B().home()   # donomethod use hogi
#     def car(self):
#         print("parent1")
# class B:
#     def home(self):
#         print("Parent2") 
#     def bank(self)   :
#         print("Parent2")  
# class C(A,B):
#     def home(self):
#         super().home()
#         print("home for child")
# obj=C() 
# obj.home()
# obj.bank()  
# obj.car()     


 #**************************  hirarical ***********************************************
# class parent1:
#     def home(self):
#         print("home for parent")
#         Child1.home(self)
# class Child1  :
#     def home(self) :
#         print("home for child1") 
#         super().home()
# class child(parent1,parent2)    :
#     def home(self) :
#         super.home()
#         print("home for child") 
# obj=child()   
# obj.home()  



#******************************************  hybrid  *********************************************

# class A:
#     def home(self):
       
#         print("home for A")
#     def car(self):
#         print("car for A")   

# class B(A):
#     def home(self) :
#         super().home() 
#         print(" home for B")  
       
# class C(A):
#     def home(self): 
#         super().home() 
#         print(" home for C")  
        
# class D(B,C):
#     def home(self): 
#         super().home() 
#         print(" home for D")  
# obj=D()
# obj1=C()   
# obj2=B()    
# obj.home()
# obj.car()
                              
   
# *******************************((((((((((((((((((((((((((  polymorphism  ))))))))))))))))))))))))))******************************************


class student









class A:
    def detail(self):
        return None
class B(A):
    def detail(self):
        return"from B class"  
class C(A):
    def detail(self):
        return"from C class"
obj1=B() 
print(obj1.detail())
obj2=C()
print(obj2.detail())   

      
   
   

