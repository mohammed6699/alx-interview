#!/usr/bin/python3
def validUTF8(data):
    # check if the given data set represents a valid UTF-8 encoding
    # return True if right
    # else, return false

    for bytes in data:
        num = 0
        while bytes & (1 << (7 - num)) != 0:
            num += 1
        if num == 0:
            continue
        elif num == 1:
            if bytes & (1 << 6) != 0:
                return False
        elif num == 2:
            if bytes & (1 << 5) != 0:
                return False
        elif num == 3:
            if bytes & (1 << 4) != 0:
                return False
        elif num == 4:
            if bytes & (1 << 3) != 0:
                return False
        else:
            return True
        # check if there are enough continuatioin bytes
        for _ in range(num - 1):
            if len(data) == 0:
                return False
            byte = data.pop(0)
            if byte & (1 << 6) == 0:
                return False
    return True
        
