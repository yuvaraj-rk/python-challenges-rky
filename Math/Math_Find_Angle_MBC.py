#https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

import math

ab = int(input())
bc = int(input())

# Calculate the angle in radians using atan2(opposite, adjacent)
# Then convert to degrees
angle_rad = math.atan2(ab, bc)
angle_deg = math.degrees(angle_rad)

# Round the result and format with the degree symbol
# The problem requires the nearest integer
print(f"{round(angle_deg)}{chr(176)}")
