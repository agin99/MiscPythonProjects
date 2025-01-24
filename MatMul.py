#Perform matrix multiplication using list comprehension
def mat_mul(m1, m2):
    res_mat = []
    for index in range(len(m1)):
        res_mat.append([0] * len(m2[0]))
    flat_res_mat = []
    flat_m1 = [item for row in m1 for item in row]
    flat_m2 = [m2[j][i] for i in range(len(m2[0])) for j in range(len(m2))]
    for col_comp_index in range(len(flat_m2)):
        list_edge = (col_comp_index + 1)*len(m2) % len(flat_m1)
        if list_edge == 0:
            list_edge = len(flat_m1)
        row = flat_m1[(col_comp_index)*len(m2) % len(flat_m1): list_edge]
        col = flat_m2[col_comp_index // len(m2) * len(m2): (col_comp_index // len(m2) + 1) * len(m2)]
        row_index = ((col_comp_index)*len(m2) % len(flat_m1)) // ((col_comp_index // len(m2) + 1) * len(m2))
        res_mat[row_index][col_comp_index % len(m2[0])] = sum([row_item * col_item for row_item, col_item in zip(row, col)])

    return res_mat