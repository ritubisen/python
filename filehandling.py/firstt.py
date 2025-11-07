# # filr handling
# ================ ('file-name-with extention' , mode)=====================
# # mode :--
# # mode arew 4 types in file handlling 
# # 1. create (x)
# # 2. write  (w)
# # 3. read   (r)
# # 4. oppend  (q)

# firstt.py*******************************



# mode |  create-new |  exiting-file |  writable  |  readable  |  cursor-position
=======================================================================================
    
#  x      |      yes       |    no            |      yes      |    no         |   oth - index               |
#  w      |      yes       |    yes           |      yes      |    no         |   oth - index               |
#  r      |      no        |    yes           |      no       |     yes       |   oth - index               |
#  a      |      yes       |    yes           |      yes      |    no         |   previous_last             |


# f = open('n3.txt','x')

# print(f.name)         #---->>   n1
# print(f.mode)         #---->>    x
# print(f.encoding)
# print(f.writable())
# print(f.readable())
# print(f.closed)



# w = open('w1.txt','w')

# print(w.name)         #---->>   n1
# print(w.mode)         #---->>    x
# print(w.encoding)
# print(w.writable())
# print(w.readable())
# print(w.closed)

# r = open('r1.txt','r')

# print(w.name)         #---->>   n1
# print(w.mode)         #---->>    x
# print(w.encoding)
# print(w.writable())
# print(w.readable())
# print(w.closed)

a = open('a1.txt','a')

print(a.name)         #---->>   n1
print(a.mode)         #---->>    x
print(a.encoding)
print(a.writable())
print(a.readable())
print(a.closed)


