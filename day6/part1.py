file = open("input.txt", "r")
data = file.readlines()

for i in range(len(data)):
    if data[i][-1] == "\n":
        data[i] = data[i][:-1]

# Locate the marker 
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "^":
            position = (i, j)
            break

locations = set()
directions = {0: [-1, 0],  
              1: [0, 1],  
              2: [1, 0],
              3: [0, -1]}
print(data)
def move(position: tuple, direction: int):
    global locations
    next_row = position[0] + directions[direction][0]
    next_col = position[1] + directions[direction][1]
    if not (0 <= next_row < len(data)) or not (0 <= next_col < len(data[0])):
        return None
    if data[next_row][next_col] != "#":
        position = (next_row, next_col)
        locations.add(position)
        return position, direction
    elif data[next_row][next_col] == "#":
        return position, (direction + 1) % 4

direction = 0

while True:
    result = move(position, direction)
    if result is None:
        break
    position, direction = result
print(len(locations)+1)