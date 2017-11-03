import cmath
# This function returns the euclidean distance between the two given points
def distance(p1, p2):
    sumatory = 0
    for i in range(len(p1)):
        sumatory += (p1[i] - p2[i])^2
    return cmath.sqrt(sumatory)