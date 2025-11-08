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
# ===========================================================================================================
      #   |                |                  |               |               |                             |
#  x      |      yes       |    no            |      yes      |    no         |   oth - index               |
#  w      |      yes       |    yes           |      yes      |    no         |   oth - index               |
#  r      |      no        |    yes           |      no       |     yes       |   oth - index               |
#  a      |      yes       |    yes           |      yes      |    no         |   previous_last             |


# f = open('n4.txt','x')

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

# a = open('a1.txt','a')

# print(a.name)         #---->>   n1
# print(a.mode)         #---->>    x
# print(a.encoding)
# print(a.writable())
# print(a.readable())
# print(a.closed)


# #====================  apend mode ============================================

# f = open('a3.txt','a')

# data = '''this is
#                python  
#                        class'''
# f.write(data)
# f.close()



# f = open('a4.txt','a')

# # data = ['python\n','java\n','html\n','cpp\n','js\n']
# # f.writelines(data)
# # f.close()

# data = 'python'
# data1 = "this is pyhton "
# data2 = '''this
#                is 
#                   pyhon'''
# # f.write(data)
# # f.write(data1)
# # f.write(data2)
# # f.close()

# # multiple line ko likhen ke liye writelines ka use hota h============

# f.writelines([data,data1,data2])
# f.close()


# f = open('a5.txt','a')

# data = 'python\n'
# data1 = "this is pyhton\n "
# data2 = '''this
#                is 
#                   pyhon\n'''
# f.writelines([data,data1,data2])
# f.close()


#*********************************************((((((((((((((((((((      READ()  (read mode)    ))))))))))))))))))))*************************************************

# 4 types of read()

# 1. read() -->>>>  read all data
# 1. read(n)  -->>>>  read n  bits of data
# 1. readlines() -->>>> single-line
# 1. readlines()   -->>>>  multiple lines of  data 

# f = open ('a5.txt')
# # data = 'python'
# all_data = f.read()
# print(all_data)
# data = f.read()
# print(data)
# f.close()



# f = open ('a5.txt')

# all_data = f.read(10)
# print(all_data)
# data = f.read()
# print(data)
# f.close()



f = open ('a5.txt')
data=f.readline()
print(data)


f = open ('a5.txt')
data=f.readlines()
print(data)

#================================================== curser movment===================================================