import cmath
# This function returns the euclidean distance between the two given points
def distance(p1, p2):
    sum = 0
    for i in range(len(p1)):
        sum += (p1[i] - p2[i])^2
    return math.sqrt(sum)