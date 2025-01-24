from fractions import Fraction as frac
from math import sqrt
from DotProduct import dot_product

def vec_sub(v1, v2):
    return [[i[0] - j[0]] for i, j in zip(v1, v2)]

def vec_add(v1, v2):
    return [[i[0] + j[0]] for i, j in zip(v1, v2)]

def vec_mul(c, v1):
    return [[c * i[0]] for i in v1]

def normalize(v1):
    mag_v = sqrt(sum([i[0]**2 for i in v1]))
    normalized_v1 = [[i[0] / mag_v] for i in v1]
    return normalized_v1

def gram_schmidt(m1):
    res_mat = []
    col_flat_m1 = [m1[col_index][row_index] for row_index in range(len(m1)) for col_index in range(len(m1[0]))]
    for i in range(len(m1[0])):
        v_to_orthogonalize = [[item] for item in col_flat_m1[i * len(m1):(i + 1) * len(m1)]]
        proj_vec_list = [vec_mul(dot_product(v_to_orthogonalize, prev_col), prev_col) for prev_col in res_mat[:i]]
        orthogonalized_v = v_to_orthogonalize
        for item in proj_vec_list:
            orthogonalized_v = vec_sub(orthogonalized_v, item)
        v_to_normalize = orthogonalized_v
        normalized_v = normalize(v_to_normalize)
        res_mat.append(normalized_v)
    return res_mat

def main(): 
    m1 = [
        [frac(1, 1), frac(2, 1)],
        [frac(4, 1), frac(1, 1)]
    ]

    orthonormalized_matrix = gram_schmidt(m1)
    for row in orthonormalized_matrix:
        print(row)

main()