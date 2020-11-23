# number of rectangles in an N × M grid is
# rect(M, N) = M * (M + 1) * N * (N + 1) / 4
#
# we can therefore try all combinations of N and M up to
# 2000000 rectangles in the grid and find the solution this way

def nearest_rectangles(k):
    """
    Finds a grid for which the number of rectangles in it is the closest
    to given number.
    :param k: an integer
    :return: n, m dimensions with the closest number of rectangles
    """
    threshold = k ** 0.5

    n = 1
    m = 1
    closest = k
    closest_nm = n, m
    rectangles = rect(n, m)
    flag = True

    while flag:
        while rectangles <= k:
            current = abs(k - rectangles)
            if current < closest:
                closest = current
                closest_nm = n, m

            n += 1
            rectangles = rect(n, m)

        m += 1
        n = m
        rectangles = rect(n, m)

        # we would only get higher numbers from now on
        if m > threshold and n > threshold:
            flag = False

    return closest_nm


def rect(n, m):
    """
    Computes number of rectangles in an n × m grid
    :param n: height of the grid
    :param m: width of the grid
    :return: number of rectangles in the grid
    """
    return (m * (m + 1) * n * (n + 1)) // 4


closest = nearest_rectangles(2000000)
print(closest[0] * closest[1])
