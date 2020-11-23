# the shortest route to the opposite corner while travelling
# only on the surfaces for cuboid with dimensions a <= b <= c is
# d = sqrt(c^2 + (a + b)^2)

def distance_to_opposite_corner(a, b, c):
    """
    Computes distance from one corner of the cuboid to the opposite one
    while travelling only on the surfaces.
    :param a: width of the cuboid
    :param b: height of the cuboid
    :param c: depth of the cuboid
    :return: distance of the opposite corners
    """
    return ((c * c) + (a + b) * (a + b)) ** 0.5


def equal(a, b, epsilon):
    """
    Determines, whether two numbers are within epsilon of each other.
    :param a: first number
    :param b: second number
    :param epsilon: allowed difference
    :return: True, if a and b are within epsilon of each other,
             False, otherwise
    """
    if abs(a - b) < epsilon:
        return True
    else:
        return False


c = 2
routes = 0

while routes < 1000000:
    c += 1
    for ab in range(3, 2 * c + 1):
        current = (c * c + ab * ab) ** 0.5
        # epsilon value is arbitrary
        if equal(current, int(current), 0.0001):
            # determines how many combinations of a + b we can get
            if ab <= c:
                # a = 1, b = ab - 1, or a = 2, b = ab - 2, etc.
                routes += (ab // 2)
            else:
                # b between upper whole part of (a + b) / 2 included and c included
                routes += (1 + (c - (ab + 1) // 2))

print(c)
