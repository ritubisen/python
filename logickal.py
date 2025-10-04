# ===============================  logical operators  on string   ==========================================
#---------------------------(and , or , not )------------------------------------

# s="java"
# s1="python"
# print(s1 and s)  # dono value true haii to output true aayega 

# s2=""
# s1="java"
# print(not s1)
# print(not s2)

# s="java"
# s1="python"
# print(s1 or s)


# =======================================================  methods for string  =================================================================

# lower()
# uper case()
# swapcase()
# title()
# capitalize()
# index()
# count()
# split()

s='pythonepythhoo1234'
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title()) 
# print(s.capitalize())
# print(s.index('n',-1))
# print(s.count("t"))
# join ==>>>  'seprator' . join(collection/iterator)
# s1='python'
# s2='java'
# s='_'.join([s1,s2])
# print(s)


#======================================================= split  ===================================================
# collevction split
#collection.split('from where')
#collection.split('from where' , 'how many time')




s="this is python class "
# print(s.split())
# print(s.split("i"))
print(s.split("i",1))

#===========================================================  replace ()  ========================================================
# syntax
# collectin . replace('old values' , 'new value' , 'how many time')
# collectin . replace('old values' , 'new value')
s="this is python class"
print(s.replace('','-'))
print(s.replace('','-',2))
# print(s.replace())
print(s)