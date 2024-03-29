#!/usr/bin/python3

"""
Function: can_unlock_all

Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
Task: Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where each inner list represents a box.

    Returns:
        bool: True if all boxes can be opened, else False.
    """

    # Number of boxes
    n = len(boxes)

    # Initialize a set to track opened boxes
    opened_boxes = {0}

    # Initialize a set to track keys
    keys = set(boxes[0])

    # Keep looping until no more new keys are found
    while keys:
        # Get a key from the set
        key = keys.pop()

        # Check if the key opens a new box
        if key < n and key not in opened_boxes:
            opened_boxes.add(key)
            keys.update(boxes[key])

    # Check if all boxes are opened
    return len(opened_boxes) == n
