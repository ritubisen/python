# //token//

# KEYWORD----------------------------
import keyword
import string

#keywords...
print("1. KEYWORDS")
print("\n")

keys = keyword.kwlist
print("this is keywords")
print(keys)
print(len(keys))

softkeys = keyword.softkwlist
print("this is soft keywords")
print(softkeys)
print(len(softkeys))

#punctuation...
print("\n")
print("2. PUNCTUATION")
print("\n")

spesyb = string.punctuation
print("this is punctuation")
print(spesyb)
print(len(spesyb))

upper = string.ascii_uppercase
print("this is uppercase")
print(upper)
print(len(upper))

lower = string.ascii_lowercase
print("this is uppercase")
print(lower)
print(len(lower))
