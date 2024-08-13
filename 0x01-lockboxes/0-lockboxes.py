#!/usr/bin/python3
"""
    lock boxes
"""
def canUnlockAll(boxes):
    """
    function to determine if the 
    boxes contain keys for the other boxes or not
    return True if all boxes opens
    return False if one of boxes doesnot open
    """
    unlock = [0]
    keys = set(boxes[0])
    while keys:
        new_keys = keys.pop()
        if new_keys not in unlock and new_keys < len(boxes):
            unlock.append(new_keys)
            keys.update(boxes[new_keys])
    return len(unlock) == len(boxes)
