import Mat_Process

while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a Determinant")
    print("6. Inverse Matrix")
    print("0. Exit")
    n = int(input("Your choice: "))
    if n == 1:
        Mat_Process.add()
    elif n == 2:
        Mat_Process.scalar_multiply()
    elif n == 3:
        Mat_Process.matrix_multiply()
    elif n == 4:
        print()
        print("1. Main Diagonal")
        print("2. Side Diagonal")
        print("3. Vertical Line")
        print("4. Horizontal Line") 
        m = int(input("Your Choice:"))
        if m == 1:
            Mat_Process.transpose_main()
        elif m == 2:
            Mat_Process.transpose_side()
        elif m == 3:
            Mat_Process.transpose_vert()
        else:
            Mat_Process.transpose_hor()   
    elif n == 5:
        mat, dim = get_inp()
        if dim[0] == dim[1]:
            print("The result is:")
            print(Mat_Process.det(mat, dim[0]))
        else:
            print("The operation cannot be performed")     
    elif n == 6:
        Mat_Process.inv()                           
    else:
        exit()            
         
