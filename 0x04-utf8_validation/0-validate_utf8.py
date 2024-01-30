#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding."""
    num_bytes = 0

    for byte in data:
        byte_str = format(byte, '#010b')[-8:]

        if num_bytes == 0:
            for bit in byte_str:
                if bit == '0':
                    break
                num_bytes += 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte_str[0] == '1' and byte_str[1] == '0'):
                return False

        num_bytes -= 1

    return num_bytes == 0
