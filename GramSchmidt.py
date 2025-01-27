from fractions import Fraction as frac
from math import sqrt
from DotProd import dot_product

def vec_sub(v1, v2):
    return [[i[0] - j[0]] for i, j in zip(v1, v2)]

def vec_add(v1, v2):
    return [[i[0] + j[0]] for i, j in zip(v1, v2)]

def vec_mul(c, v1):
    print(f"vec_mul::c: {c}")
    print(f"vec_mul::v1: {v1}")
    for i in v1:
        print(f"vec_mul::c*v1: {c*i[0]}")
    return [[c * i[0]] for i in v1]

def normalize(v1):
    mag_v = sqrt(sum([i[0]**2 for i in v1]))
    normalized_v1 = [[i[0] / mag_v] for i in v1]
    return mag_v, normalized_v1

def gram_schmidt(m1):
    res_mat = []
    col_flat_m1 = [m1[col_index][row_index] for row_index in range(len(m1)) for col_index in range(len(m1[0]))]
    r_mat = []
    mag_list = []
    for i in range(len(m1)):
        r_mat.append([frac(0, 1)]*len(m1[0]))
        r_mat[i][i] = frac(1, 1)
    for i in range(len(m1[0])):
        v_to_orthogonalize = [[item] for item in col_flat_m1[i * len(m1):(i + 1) * len(m1)]]
        # print(f"VT: {v_to_orthogonalize}")
        proj_vec_list = [vec_mul(dot_product(v_to_orthogonalize, prev_col), prev_col) for prev_col in res_mat[:i]]
        # print(f"PVL: {proj_vec_list}")
        orthogonalized_v = v_to_orthogonalize
        for item in proj_vec_list:
            orthogonalized_v = vec_sub(orthogonalized_v, item)
        # print(f"OV: {orthogonalized_v}")
        v_to_normalize = orthogonalized_v
        mag_v, normalized_v = normalize(v_to_normalize)
        # print(f"NV: {normalized_v}")
        mag_list.append(mag_v)
        # print(f"ABC: {len([dot_product(v_to_orthogonalize, prev_col) for prev_col in res_mat[:i]])}")
        # print(f"DEF: {i, [dot_product(v_to_orthogonalize, prev_col) for prev_col in res_mat[:i]]}")
        r_mat_appendage_list = [dot_product(v_to_orthogonalize, prev_col) for prev_col in res_mat[:i]]
        print(i, r_mat_appendage_list)
        for j in range(i):
            # print(f"RMA: {r_mat_appendage_list[j]}")
            r_mat[j][i] = r_mat_appendage_list[j]
        res_mat.append(normalized_v)
        r_mat[i][i] = mag_v * r_mat[i][i]

    # print(mag_list)
    adj_list = [res_mat[j][i] for i in range(len(res_mat[0])) for j in range(len(res_mat))]
    for i in range(len(res_mat[0])):
        res_mat[i] = adj_list[i * len(res_mat[0]):(i + 1) * len(res_mat[0])]
    return r_mat, res_mat

def main(): 
    m1 = [
        [frac(1, 1), frac(2, 1), frac(1, 1)],
        [frac(4, 1), frac(1, 1), frac(2, 1)],
        [frac(3, 1), frac(1, 1), frac(1, 1)],
    ]
    r_mat, res_mat = gram_schmidt(m1)
    print("")
    print("Q:")
    for row in res_mat:
        print(row)
    print("")
    print("R:")
    for row in r_mat:
        print(row)
    print("")

main()