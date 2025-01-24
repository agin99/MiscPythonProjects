from fractions import Fraction as frac
from LUDecomp import lu_decomp, det

def ver_nonzero_det(m1):
    p_matrix, u_matrix, l_matrix = lu_decomp(m1)
    diag_list = [l_matrix[i][i] for i in range(len(l_matrix))]
    return diag_list, l_matrix, det(l_matrix) == 0

def poly_mul(p1, p2):
    res_poly = [0]*(len(p1) + len(p2) - 1)
    for p1_index, i in enumerate(p1):
        for p2_index, j in enumerate(p2):
            res_poly[p1_index + p2_index] += i*j
    return res_poly

def setup_char_eq(diag_list):
    char_eq_list = [[-diag_item, frac(1, 1)] for diag_item in diag_list]
    char_eq = char_eq_list.pop(0)
    for char_term in char_eq_list:
        char_eq = poly_mul(char_eq, char_term)
    return char_eq

def qr_decomp():
    pass 

def main(): 
    m1 = [
        [frac(2, 1), frac(2, 1)],
        [frac(1, 1), frac(1, 1)]
    ]
    diag_list, l_matrix, outcome = ver_nonzero_det(m1)
    char_eq = setup_char_eq(diag_list)

    # p1 = [1, 1] #x + 1
    # p2 = [1, 1] #x + 1
    
    # res_p = poly_mul(p1, p2)
    # print(res_p)

main()