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
#  class 
# object 
# constructor 
# self


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



class student :
      school_name='cyrome'
      def __init__(self,name,rollno):                                  #  inside
          self.n,self.r=name,rollno               # decalartion
          student.gread = '10th'
      def addnew(self):
          student.principle="python"

student.school_city="bhopal"
obj=student('ritu',987)  
obj.addnew()                                  