Tom={"sem1":["A","S","C","D","B","A"],
      "sem2":["B","A","S","S","C","B"],
       "sem3":["C","B","N","F","A","S"]}
std_names=("Tom","Jerry")
std_sgpa={}
std_cgpa={}
no_of_stds=1

for i in range(no_of_stds):
    sgpa_l=[]
    name=std_names[i]
    for sem in Tom:
        SGPA=0.0
        for grade in Tom[sem]:
            if grade=="S":
                SGPA+=10
            elif grade =="A":
                SGPA+=9
            elif grade=="B":
                SGPA+=8
            elif grade =="C":
                SGPA+=7
            elif grade =="D":
                SGPA+=6
            elif grade =="E":
                SGPA+=5
            else:
                SGPA+=4
        SGPA /=len(Tom[sem]) 
        sgpa_l.append(SGPA) 
    std_sgpa[f"{name}_SGPAs"] = sgpa_l
    
print(std_sgpa) 
  
CGPA=0.0
for name in std_sgpa:
    for sgpa in std_sgpa[name]:
        CGPA += sgpa
    CGPA/=len(Tom)
    temp=name[:-6]
    std_cgpa[f"{temp}_CGPA"]=CGPA
print(std_cgpa)       
        
        
                                      