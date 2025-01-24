#Compute dot product using list comprehension
def dot_product(v1, v2):
    return sum([i[0]*j[0] for i,j in zip(v1,v2)])