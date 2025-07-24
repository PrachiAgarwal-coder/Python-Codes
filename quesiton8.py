str1="vit"
str2="vit"

if(str1==str2):
    print("Both are same")
else:
    print("Not same")    
    
print("Geek"<"geek")    
print("Geek">"geek")

print("Geek"!= "Geek")
print("Abhi"!= "VIT")

str3= 'vit'
str4= 'vit'
print(id(str3),id(str4))
print(str3 is str4)

str5= 'vit'
str6=(str5 + '.')[:-1]
print(id(str5),id(str6))
print(str5==str6)
print(str5 is str6)

if str5 is not str6:
    print("str5:",str5)
    print("str6:",str6)
else:
    print("They are the same instance") 
    
    print(25*"=")   