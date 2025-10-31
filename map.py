#====================================  map()  =============================================
# collection of array


# syntax :-

# collection (d,f,t,e)

# def fun_name():
#     fun_body
# list(map(fun_name, collection))    


#q.1.================================================================

l=[1,2,3,4,5]

def squar(n):
    return n*n
result=map(squar,l)
print (result)
print(list(result))
