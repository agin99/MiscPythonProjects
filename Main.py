import fractions
from LUDecomp import lu_decomp, det, solver

def main():
    m1 = [
        [fractions.Fraction(0, 1), fractions.Fraction(1, 1), fractions.Fraction(1, 1), fractions.Fraction(1, 1)], 
        [fractions.Fraction(1, 1), fractions.Fraction(0, 1), fractions.Fraction(1, 1), fractions.Fraction(5, 1)],
        [fractions.Fraction(2, 1), fractions.Fraction(1, 1), fractions.Fraction(1, 1), fractions.Fraction(0, 1)],
        [fractions.Fraction(15, 1), fractions.Fraction(0, 1), fractions.Fraction(3, 1), fractions.Fraction(7, 1)]
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
        [3],
        [2]
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