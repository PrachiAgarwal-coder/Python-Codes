str1 = "vit"
print(str1[1])

str2 = "vit vellore"
print(str2[4:11])
print(str2[-7:0])

sentence = "I study in Vit"
university = sentence[-3:]
print(university.upper())
print(university.lower())

str1="vit.vellore"
print(str1.split(" "))

str2="my name is vit"
print(str2.split('m'))

str3="hello world lol"
print(str3.split("lo"))
 
str1= "      hello world "
str2= str1.lstrip()
print(str2,len(str2))

string = "the king has the largest army in the entire world"
print(string.strip("the"))
 
string =" the king has the largest army in the entire world"
print(string.strip("the"))

str1="vit vallora"
print(str1.replace("a","e"))
