#!/usr/bin/python3
"""
    pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of integer 
    representing the pascal triangle
    returns empty list if n <= 0
    """

    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            if j < len(triangle[i-1]):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            else:
                break
        row.append(1)
        triangle.append(row)
    return triangle
