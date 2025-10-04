# # method of lists  =>  collection of elements  
                         #|# 

# there are two types in list 
# 1. homogeneous(same data type)
# 2. hetrogeneous(diffrent data type)

# ==>>>> represented by [] with comma(,) seperates elements.set
# ==>>>  orderd collection.
# ==>> indexing supported.
# ==>> slicing supported
# ==>> mutable nature 



# m=[10,10,20,30]
# print(m.count(10))
# print(m.count(100))    #calculate frequency

# m.sort()
# print(m)

# m.reverse()
# print(m)

#arrange descending
# s=[10,20,50,60]
# s.sort()
# s.reverse()
# print(s)


#one more way to arrange descending
# s=[10,20,50,60]
# s.sort(reverse=True)
# print(s)

# t=[1,2,3,4,5,5]
# t1=t.copy()
# print(t)
# print(t1)
# print(id(t),id(t1))

# t.clear()
# print(t)

# #yaha pee hamne clear method ko ek variable me store krdiya heee
# t.clear()
# x=t
# print(t)
# print(id(t))

#.....................
# del t
# print(t)
# # colletion of orderd homogenuous as well as hetrogeneriouus elemtns
#indexing supported
#slicing supported
#immutable in nature

# # inbuilt functions apply in tuple
# t=('python','java')
# print(max(t))
# print(min(t))


# s=(10,10.5,20)
# print(sum(s))


# # inbuilt methods of tuple
# a=(10,10,20,30,'python',40)
# print(a.index('python'))
# # print(a.index('python',5))   yeh error generate krega qkiii yaha 5th index m kuch nahi he
# print(a.count(10))



#-=======================================list ========================================
# my_list=[10,10.5,'python',[1,2,4],(1,2,3,4),{'x':10}]
# print(my_list)
# print(type(my_list))
            
            #  python in-built function for list 

           # 1. len() ----->  print(len(l))
           # 2. max() ----->  print(max(l))
           # 3. min() ----->  print(min(l))
           # 4. sum() ----->  print(sum(l))
           # 4. print() ----->  print(l)
           # 4. type() ----->  print(type(l))
           # 4. id() ----->  print(id(l))
          

l=[22,33,44,55,66]
print(len(l))
print(max(l))
print(min(l))
print(sum(l))
print(l)
print(type(l))
print(id(l))


#   h,w  =========   operator check krna h list per