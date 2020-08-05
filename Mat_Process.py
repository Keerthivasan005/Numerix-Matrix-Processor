#function to get the dimension for the matrix
def inp_dim():
    dim = input("Enter size of matrix: ")
    dim = dim.split()           #split function splits it into string array eliminates the spaces
    dim[0] = int(dim[0])
    dim[1] = int(dim[1])
    return dim    

#function to get input for the matrix
def inp_mat(dim):
    print("Enter matrix: ")
    mat = []
    for col in range(dim[0]):           
        m1 = input()
        m1 = m1.split()
        for i in range(len(m1)):
            m1[i] = float(m1[i])
        mat.append(m1)
    return mat  
 
def get_inp():          
    dim = inp_dim()
    mat = inp_mat(dim)
    return mat, dim
    # dim_2 = inp_dim()
    # mat2 = inp_mat(dim_2)

#function to add the matrices
def add():    
    mat1, dim_1 = get_inp()
    mat2, dim_2 = get_inp()
    if dim_1 == dim_2:
        print("The result is:")
        #add = mat1 + mat2
        for i in range(dim_1[0]):
            for j in range(dim_1[1]):
                print(mat1[i][j] + mat2[i][j], end=' ')
            print()        
    else:
        print("The Operation cannot be performed")

#function that multiplies a scalar to a matrix
def scalar_multiply():
    mat, dim = get_inp()
    k = int(input())
    print("The result is:")
    for i in range(dim[0]):
        for j in range(dim[1]):
            print(k * mat[i][j], end=' ')
        print()   

#function that multiplies matrices 
def matrix_multiply():
    mat1, dim_1 = get_inp()
    mat2, dim_2 = get_inp()
    if dim_1[1] == dim_2[0]:
        print("The result is:")
        for i in range(dim_1[0]):
            for j in range(dim_2[1]):
                sum = 0
                for k in range(dim_2[0]): 
                    sum = sum + (mat1[i][k] * mat2[k][j])
                print(sum, end=' ')
            print()   
    else:
        print("The operation cannot be performed")

#functions that prints the transpose of matrix along different dimensios          
def transpose_main():
    mat, dim = get_inp()
    if dim[0] == dim[1]:
        print("The result is:")
        for i in range(dim[0]):
            for j in range(dim[1]):
                print(mat[j][i], end=' ')
            print()    
    else:
        print("The operation cannot be performed")            
            
def transpose_side():
    mat, dim = get_inp()
    if dim[0] == dim[1]:
        print("The result is:")
        for i in range(dim[0]):
            for j in range(dim[1]):
                print(mat[dim[0] - j - 1][dim[1] - i - 1], end=' ')
            print()
    else:
        print("The operation cannot be performed")      
        
def transpose_vert():
    mat,dim = get_inp()
    print("The result is:")
    for i in range(dim[0]):
        for j in range(dim[1]):
            print(mat[i][dim[1] - j - 1], end=' ')
        print()
        
def transpose_hor():
    mat, dim = get_inp()
    print("The result is:")
    for i in range(dim[0]):
        for j in range(dim[1]):
            print(mat[dim[0] - i - 1][j], end=' ')
        print()    
                                   
#function to find the determinant                                   
def det(mat, dim):
    if dim == 1:
        return mat[0][0]
    if dim == 2:
        return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])
    det_ = 0    
    for i in range(dim):
        new_mat = []
        for j in range(dim):
            if j != i:
                new_mat.append(mat[j][1:])
        if i % 2 == 0:
            det_ += mat[i][0] * det(new_mat, dim - 1)
        else:
            det_ -= mat[i][0] * det(new_mat, dim - 1)
    return det_
    
def cofactor(mat, dim, p,q):
    new_mat = []
    for i in range(dim):
        n = []
        for j in range(dim):
            n.append(mat[i][j])
        new_mat.append(n)
    for k in range(dim):        
        new_mat[k].pop(q)
    new_mat.pop(p)    
        
    return det(new_mat,dim-1)              
   
def round_(element):
    if element > 0:
        element *= 100
        element = element // 1
        element /= 100      
    return element
    element *= -100
    element = element // 1
    element /= -100
    return element
                       
def inv():
    mat, dim = get_inp()
    inv_mat = []
    if det(mat, dim[0]) != 0:
        print("The result is:")
        for i in range(dim[0]):
            n = []
            for j in range(dim[0]):
                if cofactor(mat, dim[0], j, i) == 0:
                    n.append(0)
                else:        
                    element = cofactor(mat, dim[0], j ,i) / det(mat, dim[0]) * pow(-1, i + j)
                    n.append(round_(element))
            inv_mat.append(n)
        for i in range(dim[0]):
            for j in range(dim[0]):
                if inv_mat[i][j] > 0:
                    print(f" {inv_mat[i][j]}", end = ' ')
                elif inv_mat[i][j] < 0:
                    print(f"{inv_mat[i][j]}", end = ' ')
                else:
                    print("  0 ", end = ' ')        
            print()
              
    else:
        print("This matrix doesn't have inverse")


