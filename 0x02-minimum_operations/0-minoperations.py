#!/usr/bin/python3
"""
    Minimum Operations
"""

def minOperations(n:int) -> int:
    """
        the fewest number of operations needed to result in exactly 
    """

    body = 'H'
    next ='H'
    ops = 0

    while (len(body) < n):
        if (n % len(body) == 0):
            ops +=2
            next = body
            body += body
        else:
            ops += 1
            body += next

        if (len(body) >= n):
            return ops
        return 0
