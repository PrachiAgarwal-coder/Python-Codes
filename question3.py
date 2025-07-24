
citizen = ("Tom", 123456, "A+")
print(citizen)


print(citizen[0],citizen[2])

for elem in citizen:
    print(elem)
    
citizen.append(987654321)

citizen[2] = "B-"

citizen_twice=citizen*2
print("citizen_twice")

if("A+" in citizen):
    print("Citizen's blood group is A+")
    
