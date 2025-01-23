import fractions
from MatMul import mat_mul

def lu_decomp(matrix):
    remaining_indices = []
    permutation_matrix = []
    lower_triangular_matrix = []
    operation_tracker = []
    #Construct initial matrix structures
    for i in range(len(matrix)):
        remaining_indices.append(i)
        permutation_matrix.append([fractions.Fraction(0,1)]*len(matrix))
        permutation_matrix[i][i] = fractions.Fraction(1,1)
        lower_triangular_matrix.append([fractions.Fraction(0,1)]*len(matrix))
        lower_triangular_matrix[i][i] = fractions.Fraction(1,1)
        operation_tracker.append([])
    for col_index in range(len(matrix)):
        ref_index = remaining_indices[0]
        subsequent_max_row = []
        #Compute leading value for partial pivot in col_index of REMAINING rows in INPUT matrix - DONE
        for index, row in enumerate(matrix):
            if index in remaining_indices: 
                if abs(row[col_index]) >= (abs(subsequent_max_row[col_index]) if len(subsequent_max_row) > 0 else 0):
                    subsequent_max_row = row
        #Save leading term and leading row for row operations - DONE  
        leading_term = subsequent_max_row[col_index]
        leading_row = subsequent_max_row

        #Swap leading permutation row with top row - DONE
        temp_perm_row = permutation_matrix[matrix.index(subsequent_max_row)]
        permutation_matrix[matrix.index(subsequent_max_row)] = permutation_matrix[col_index]
        permutation_matrix[col_index] = temp_perm_row
        temp_op_row = operation_tracker[matrix.index(subsequent_max_row)]
        operation_tracker[matrix.index(subsequent_max_row)] = operation_tracker[col_index]
        operation_tracker[col_index] = temp_op_row
        #Swap leading row with top row - DONE
        matrix[matrix.index(subsequent_max_row)] = matrix[col_index]
        matrix[col_index] = leading_row
        remaining_indices.remove(matrix.index(subsequent_max_row))

        #Update LOWER TRIANGULAR matrix at 'reverse operation index'
        for index, row in enumerate(matrix):
            if index in remaining_indices:
                operation_tracker[index].append(row[col_index] / leading_term)
                matrix[index] = [j - row[col_index] / leading_term * i for i,j in zip(leading_row, row)]
    for row_index, row in enumerate(operation_tracker):
        for col_index, col in enumerate(row): 
            lower_triangular_matrix[row_index][col_index] = col
        
    return permutation_matrix, lower_triangular_matrix, matrix

def det(matrix):
    det = 1
    for i in range(len(triangle_matrix)):
        det *= triangle_matrix[i][i]
    return det 

def solver(p_mat, l_mat, u_mat, b_vec): 
    pb_vec = mat_mul(p_mat, b_vec)
    ly_vec = []
    ux_vec = []
    #Solve Ly = b for y
    for row_index, row in enumerate(l_mat):
        ly_term = pb_vec[row_index][0] - sum([i[0]*j for i, j in zip(ly_vec, row[0:row_index])])
        ly_vec.append([ly_term])
    #Solve Ux = y for x
    for row_index, row in enumerate(u_mat):
        ux_term = ly_vec[len(u_mat) - row_index - 1][0] - sum([i*j for i, j in zip(ux_vec, row[len(u_mat) - row_index - 1:])])
        ux_vec.insert(0, ux_term)
    return ux_vec

def main():
    m1 = [
        [fractions.Fraction(0, 1), fractions.Fraction(1, 1), fractions.Fraction(1, 1)], 
        [fractions.Fraction(1, 1), fractions.Fraction(0, 1), fractions.Fraction(1, 1)],
        [fractions.Fraction(2, 1), fractions.Fraction(1, 1), fractions.Fraction(1, 1)]
    ]
    permutation_matrix, lower_triangular_matrix, upper_triangular_matrix = lu_decomp(m1)
    print("")
    print("Permutation matrix:")
    for row in permutation_matrix:
        print(row)
    print("")
    print("Lower triangular Matrix:")
    for row in lower_triangular_matrix:
        print(row)
    print("")
    print("Upper triangular Matrix:")
    for row in upper_triangular_matrix:
        print(row)
    print("")

    # print("")
    # for row in permutation_matrix:
    #     print(row)

    # v1 = [
    #     [1], 
    #     [0], 
    #     [1]
    # ]
    # print(f"adj_vec: {mat_mul(permutation_matrix, v1)}")
    # print("")
    
    # m2 = [
    #     [fractions.Fraction(1, 1), fractions.Fraction(1, 1)],
    #     [fractions.Fraction(2, 1), fractions.Fraction(5, 1)]
    # ]
    # permutation_matrix, lower_triangular_matrix, upper_triangular_matrix = lu_decomp(m2)
    # print("Permutation matrix:")
    # for row in permutation_matrix:
    #     print(row)
    # print("Lower triangular Matrix:")
    # for row in lower_triangular_matrix:
    #     print(row)
    # print("Upper triangular Matrix:")
    # for row in upper_triangular_matrix:
    #     print(row)
    # v2 = [
    #     [1], 
    #     [0]
    # ]
    # print(f"adj_vec: {mat_mul(permutation_matrix, v2)}")
    # print("")
    b_vec = [
        [1],
        [5],
        [3]
    ]

    print("b:")
    for row in b_vec:
        print(row)

    solution_vec = solver(
        permutation_matrix, 
        lower_triangular_matrix, 
        upper_triangular_matrix, 
        b_vec
    )
    print(solution_vec)

main()