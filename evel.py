# input()   vs    eval()=========================================

#  ye input ke liye hai ==  input => bydefault it returns string datatype 
# x=input("Enter any value")
# print(x,type(x))


# ye eval ke liye hai   ==  eval => 
x=eval(input("Enter any value : "))
print(x,type(x))