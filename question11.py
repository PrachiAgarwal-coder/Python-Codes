string=input("Enter a phrase or a sentence:")
l_string=string.lower()
string_list=l_string.split(" ")
print(string_list)

words={}
for x in string_list:
    if x in words:
        words[x]+=1
    else:
        words[x]=1
print(words)
temp=0
multiple= False
for x in words:
    if words[x]>temp:
        max=x
        temp=words[x]
    elif words[x]==temp:
        multiple=True
    else:
        pass
    if multiple==True:
        print("Multiple words have greatest number of occurances")
    else:
        print("The word\"",max,"\"occurs",temp,"times and")            
           
