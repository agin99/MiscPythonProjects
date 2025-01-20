#Perform matrix multiplication using list comprehension
def mat_mul(m1, m2):
    if len(m1) != len(m2[0]):
        print(f"Matrix dimensions don't aren't properly matched: \nm1: {len(m1[0])} x {len(m1)}\nm2: {len(m2[0])} x {len(m2)}")
        return
    
    matrix = []
    for x in range(len(m2[0])):
        matrix.append([])

    for i in range(len(m2[0])):
        vec_elem = []
        for j in range(len(m1)):
            sum_elem = 0
            for k in range(len(m1[0])):
                sum_elem += m1[j][k] * m2[k][i]
            matrix[j].append(sum_elem)
    return matrix

def main():
    m1 = [
        [2, 1, 1], 
        [0, 1, 2],
        [1, 1, 1]
    ]
    m2 = [
        [1, 1, 0], 
        [0, 1, 1],
        [1, 0, 1]
    ]
    matrix = mat_mul(m1, m2)
    for vec in matrix:
        print(vec)

main()