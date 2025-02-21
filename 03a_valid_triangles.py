# This function that takes a list of triangles.
# Each triangle is represented as a list e.g. [10, 12, 22] where the three
#  numbers are the sides of the triangle.
# The function should return the count of triangles that are valid.
# To be a valid triangle, the sum of any two sides must be larger than the
#  remaining side


def valid_triangles(triangles):

    list_valid = [1 for lst_triangle in triangles if lst_triangle[0] + lst_triangle[1] > lst_triangle[2]]

    return sum(list_valid)