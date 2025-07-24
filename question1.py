# 3 rows x 2 cols
matrix= [ [2,3],[4,5],[6,7]]
print(matrix)

# 3x3 identity matrix
identity = [[1,0,0],[0,1,0],[0,0,1]]
print (identity)

# 3x3
matrix_A = [[10,20,20],[40,51,60],[70,80,91]]
print(matrix_A)

# matrix_B = matrix_A + identity
matrix_B= [[0,0,0],[0,0,0],[0,0,0]]

nrows = ncols = 3
for i in range(0,nrows): #0,1,2
    for j in range(0,ncols): #0,1,2
        matrix_B[i][j] = matrix_A[i][j]+identity[i][j]
print(matrix_B)

print("\n") #Style 1
for i in range(nrows):
    for j in range(ncols):
        print(matrix_B[i][j], end="\t")
    print()
print("\n") #Style 2
for i in range(nrows):
    print("|", end='\t')
    for j in range(ncols):
        print(matrix_B[i][j], end="\t")
    print("|")    