empty_dict = {}
print(len(empty_dict))

fruitbasket = {"apple":3,"banana":5,"cherry":50}
print(len(fruitbasket))

oxford_dict = {"gentrification":"meaning of gentrification"}
print(oxford_dict["gentrification"])

numeric_dict = {1:1, 2:4, 3:9}
print(numeric_dict[2])

student = {'name':'Abraham','dept':'SENSE','aadhar':123456}

student['aadhar']=999999

print(student['name'], student['aadhar'])

student = {'name':'Abraham', 'dept':'SENSE','aadhar':123456}
student["city"]= 'Vellore'

print(student)
print(student['city'])
del student['aadhar']
print(student)

student['belongings']=['watch','bag','suticase','phone','laptop']

print(student['belongings'])
print(student)

student.clear()
print(student)
