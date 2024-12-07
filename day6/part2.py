file = open("input.txt", "r")
data = file.readlines()

for i in range(len(data)):
    if data[i][-1] == "\n":
        data[i] = data[i][:-1]
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "^":
            start_position = (i, j)
            break

directions = {0: [-1, 0],
              1: [0, 1],
              2: [1, 0],
              3: [0, -1]}

def move(position, direction, visited):
    next_row = position[0] + directions[direction][0]
    next_col = position[1] + directions[direction][1]
    if not (0 <= next_row < len(data)) or not (0 <= next_col < len(data[0])):
        return "Broke-out"
    if data[next_row][next_col] == "#":
        return position, (direction + 1) % 4
    if ((next_row, next_col), direction) in visited:
        return "Looped"
    position = (next_row, next_col)
    visited.add((position, direction))
    return position, direction

count = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if (i, j) == start_position or data[i][j] == "#":
            continue
        original = data[i][j]
        data[i] = data[i][:j] + "#" + data[i][j+1:]
        position = start_position
        direction = 0
        visited = set()
        visited.add((position, direction))
        while True:
            result = move(position, direction, visited)
            if result == "Looped":
                count += 1
                break
            if result == "Broke-out":
                break
            position, direction = result
        data[i] = data[i][:j] + original + data[i][j+1:]

print(count)
