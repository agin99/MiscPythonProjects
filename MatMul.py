#Perform matrix multiplication using list comprehension
def mat_mul(m1, m2):
    res_mat = []
    for index in range(len(m1)):
        res_mat.append([0] * len(m2[0]))
    flat_res_mat = []
    flat_m1 = [item for row in m1 for item in row]
    flat_m2 = [m2[i][j] for i in range(len(m2)) for j in range(len(m2[0]))]
    print(f"FL_1: {flat_m1}")
    print(f"FL_2: {flat_m2}")
    
    if len(m1[0]) != len(m2):
        print(f"Matrix dimensions don't aren't properly matched: \nm1: {len(m1)} x {len(m1[0])}\nm2: {len(m2)} x {len(m2[0])}")
        return
    else: 
        print(f"Matrix dimensions: \nm1: {len(m1)} x {len(m1[0])}\nm2: {len(m2)} x {len(m2[0])}")

    # res_mat[index % len(m2)][index // len(m2)] = sum([i for i in flat_res_mat[index * len(flat_m2): index * len(flat_m2) + len(flat_m2)]])
    print(len(m2))

def main():
    m1 = [
        [2, 1, 1], 
        [0, 1, 2],
        [1, 1, 1]
    ]
    m2 = [
        [1, 1], 
        [0, 0],
        [1, 1]
    ]
    matrix = mat_mul(m1, m2)
    # for vec in matrix:
    #     print(vec)

main()

# res_mat[index % len(m2)][index // len(m2)] = sum([i for i in flat_res_mat[index * len(flat_m2): index * len(flat_m2) + len(flat_m2)]])