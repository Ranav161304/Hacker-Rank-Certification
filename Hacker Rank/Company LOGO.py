#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input().strip()
    frequency = {}
    
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Sort by descending frequency, then by ascending character
    sorted_chars = sorted(frequency.items(), key=lambda item: (-item[1], item[0]))
    
    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")
