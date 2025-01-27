def dot_product(v1, v2):

    for i, j in zip(v1, v2):
        print(i[0], j[0])
    return sum([i[0]*j[0] for i,j in zip(v1,v2)])