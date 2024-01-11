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

    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for key in range(1, len(boxes) - 1):
        checked_boxes = False
        for index in range(len(boxes)):
            checked_boxes = key in boxes[index] and key != index
            if checked_boxes:
                break
        if checked_boxes is False:
            return checked_boxes
    return True
