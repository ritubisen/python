# #collection of key value pairs
# # key must be unique
# # value may be duplicate

# d={'name': 'ritu' , 'age':20,'quali':'bca'}
# d={2: 'ritu' , 2:20}
# d={1:20 , 2:30 , 3: 40}
# # d={'1':20 , '2':30 , '3':40}   #error show krega !
# print(len(d))
# print(max(d))
# print(min(d))  
# print(sum(d))
# print(type(d))
# print(id(d))
# print(d)





#dictionary methods==============






# 

# d={'name':'ritu','age':20,'city':'bhopal'}
# d1={'name':'sim','age':20,'city':'bhopal'}
# print(d.keys())
# print(d.values())
# print(d.items())

# # print(d.pop('city'))
# print(d.popitem())
# print(d)

# d. # for check all values

#-=========================================================== fromkeys ============================================================

# l=[2,3,4,4,'d','r','d']
# # d1=dict.fromkeys(iterator , defoult_value)
# d1=dict.fromkeys(l)    #-
# d1=dict.fromkeys(l,50)    #- ===  fromkeys
# print(d1)              #-
# print(type(d1))    #-

# #-============================================================  setdefault  =======================================================
# d1={'x':10 , 'y':20 , 'z':40}
# d = d1.setdefault('x', 100)
# d = d1.setdefault('name', 'ritu')
# print(d1)



#-======================================================= update  ======================================================
# d1={'x':10 , 'y':20 , 'z':40}
# d2={'p':50 , 'q':60 , 'r':80}
# d = d1.update(d2)
# print(d1)      


# d={'name': 'ritu' , 'age':20}
# _ = 10
# print(_)

# type = 20 
# print(type)

# match = 77
# print(match)

# case = 66
# print(case)
#==================================   set =================================================
#==>>   collection of unique elements 
#==>>   crepresnted by {}with comma(,) seperated elements
#==>>   unordered collection
#==>>   indexing not supported
#==>>   slicing not supported
#==>>   mutable im nature


# my_set = {2,4,'pyhton',3,4,'java'}
# print(my_set)
# print(type(my_set))


# # my_set ={ 'python',10,20,20,'java','php'}
# my_set ={'x','y','z',10,20,20,'j','p'}
# print(my_set)
# # inbuilt functions=====================
# print(type(my_set))
# print(id(my_set))
# print(len(my_set))
# print(sum(my_set)) #=
# print(min(my_set))      #=    ye tino error show krenge kyuki ye python ke function hai
# print(max(my_set)) #=

#set or frozenset duplicate value count  nhi krta hai python  me








#========================================= frozenset ===============================================
# collection of unique elements
# repesents by { } with (,) seprated elements
# unordered collection
#indexing not supported
#immutable in nature





l=[1,2,3,'python']
fs = frozenset(l)
print(fs)
# print(type(fs))
# print(id(fs))
# # print(sum(fs))
# # print(max(fs))
# # print(min(fs))
# print(len(fs))
fs1=frozenset({11,22,44,"python"})
fs2=frozenset({1,2,4,"python","java"})
print(fs1.union(fs2))
print(fs1.intersection(fs2))
print(fs1.difference(fs2))
print(fs1.symmetric_difference(fs2))
print(fs1.isdisjoint(fs2))
print(fs1.issubset(fs2))
print(fs1.issuperset(fs2))


#==============================================  boolean =========================================


x=True
print(x)
print(type(x))

y=None
print(y)
print(type(y))


z=range(10)
print(z)
print(type(z))













#====================================== variable declairation ===============================

# 1.   single line 
# x , y , z = 10 , 20 ,30,
# print(x)
# print(y)
# print(z)
# print(x,y,z)

# 2.  multi line 
# x=y=z=10
# print(x,y,z)

# print ("hello" , "hi" , sep="" , end='/n')
# print ("hello" , "hi" , sep="," , end='/n')

# print("hello" , end="")
# print("hii" )


#================================================  get  ===========================================

# d={'x': 10 , 'y':20 , 'z':40}
# # print(d.get('x'))
# # print(d.get('xyz' , 'guest'))

# #=====================================================  keys ========================================================

# print(d.keys())
# print(d.values())
# print(d.items())

# #=================================================== copy  =====================================================================

# d1 = d.copy()
# print(d1 , d)
# print(id(d1) , id(d))

# #===========================================================  clear  ============================================

# d.clear()
# print(d)  # isme empaty  aayega  
# print(id(d))  #  isme addresss show hoga 
# print(type(d))

#==================================================  delete  ===================================================================

# del (d)
# print (d)  

#   isme d delete ho jayega or iska use  delete ke liye krte hai 

#=====================    dir  isse ham saari methods dekh skte hai ===================================================

# print(dir(list))
# print(dir(int))
# print(dir(dict))
# print(dir(tuple))

#   isme kisi bhi keyword ki sari mrthods ham dekh skte hai  

#           ===========================================  ven diagram ========================

# s1={1,2,3,4,5,6}
# s2={4,5,6,7,8,9}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))
# print(s2.symmetric_difference(s1))