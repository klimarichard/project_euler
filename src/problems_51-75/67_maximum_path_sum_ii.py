def parse_triangle(triangle):
    """
    Parse triangle from string to a list of lists.
    :param triangle: a string with the triangle
    :return: parsed triangle
    """
    line_split = triangle.split('\n')
    number_split = [s.split(' ') for s in line_split]

    return [[int(n) for n in s] for s in number_split]


def maximum_path(triangle):
    """
    Returns maximum path from top to bottom of given triangle.
    :param triangle: a string with the triangle
    :return: maximum path from top to bottom of the triangle
    """
    triangle = parse_triangle(triangle)

    for i in range(1, len(triangle)):
        # edges only increment with the value directly above it also on the edge
        triangle[i][0] = triangle[i - 1][0] + triangle[i][0]
        triangle[i][i] = triangle[i - 1][i - 1] + triangle[i][i]

        for j in range(1, i):
            triangle[i][j] = max(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]

    # the maximum path is the maximum value from the bottom row
    return max(triangle[len(triangle) - 1])


with open('../../res/p067_triangle.txt', 'r') as f:
    triangle = f.read()

print(maximum_path(triangle))
