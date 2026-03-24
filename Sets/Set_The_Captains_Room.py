#https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

# Read K
k = int(input())

# Read the room numbers as a list of integers
rooms = list(map(int, input().split()))

# Create a set of unique room numbers
unique_rooms = set(rooms)

# Apply the mathematical formula
# Sum of unique rooms multiplied by K
# Minus the actual sum of the list
# Divided by (K - 1)
captain_room = (sum(unique_rooms) * k - sum(rooms)) // (k - 1)

print(captain_room)
