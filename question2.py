while (True):
    s = ''
    print("Enter the details for matrix 1")
    rows_1=int(input("Enter the numbers of rows:"))
    cols_1=int(input("Enter the numbers of columns:"))
    
    print("Enter the details for matrix 2")
    rows_2=int(input("Enter the numbers of rows:"))
    cols_2=int(input("Enter the numbers of columns:"))
    
    if cols_1==rows_2:
        break
    else:
        print("Cannot multiply the two matrices")
        print("No. of cols of matrix 1 should be equal to no.of rows in matrix 2")
        print("If you wish to end the program, type \"end\"")
        s=input("Type anyhting else to continue")
        if s=="end": break
        
if s=="end":
    print("Thank You!")
else:
    print("Enter the elements of Matrix 1:")
    matrix_1 = [[int(input())for x in range(cols_1)]for y in range(rows_2)] 
    print(matrix_1) 
    
    print("Enter the elements of Matrix 2:")
    matrix_2=[[int(input())for x in range(cols_2)] for y in range(rows_1)]  
    print(matrix_2)
    
    matrix_result = [[0 for_ in range(cols_2)] for_ in range(rows_1)]
    print(matrix_result)
for i in range(rows_1):
    for j in range(cols_2):
        for k in range(cols_1):
            matrix_result[i][j]+=matrix_1[i][k]*matrix      
   

              
    