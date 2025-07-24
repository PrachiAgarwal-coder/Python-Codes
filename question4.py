myset = {1,2,3}         
print(myset, type(myset), len(myset))

myset={1,2,3,3,2}
print(myset, len(myset))

mylist = [1,2,3,3,2]
mylist = list(set(mylist))
print(mylist)

myset = {"vit","vellore","python","vit"}
print(myset)


print(myset[0])


for elem in myset:
    print(elem)
    
" " "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"""


myset={1,2,3}
myset.add(100)
print(myset)

mylist=[200,300,400]
myset.update(mylist)
print(myset)

mystring="vit" 
myset.update(mystring)
print(myset)

myset.add(mystring)
print(myset)

myset.remove(200)
print(myset)

first_element= myset.pop()
print(first_element)
print(myset)
