name="website"
errorno=100

str1="The"  +str(name)+  "has an error number" +str(100)
print(str1)

str2="the {} is a student with reg.no {}"
print(str2.format("Tom",249876))

str3="the {0} has an error number {1}"
print(str3.format(name,errorno))

print('{2} {1} {0}'.format('directions' , 'the', 'Read'))
print("the {var1} had an error number{var2}".format(var1="website", var2=errorno))

student = "Tom"
age= 16
height= 178.32

print(f"{student} is {age} years old and is {height}cms tall")
print(f"{student} is {age} years old and is {height:1f}cms tall")
