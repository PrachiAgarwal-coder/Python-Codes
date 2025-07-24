student={'name':'Abraham','dept':'SENSE','aadhar':123456}

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

print(student.get("phone"))
if(student.get("phone")==None):
    if(student.get("phone")==None):
        phone_number=int(input("Enter your phone number:"))
        student["phone"]=phone_number
        print(student)
        for key in list(student.keys()):
            print(key)
        for val in list(student.values()):
            print(val)
        print(student.items()) 
        
        for key,val in list(student.items()):
            print(key,val)  
            
        